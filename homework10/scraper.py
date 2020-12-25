import asyncio
import datetime
import json
from urllib.parse import urljoin

import aiohttp
from bs4 import BeautifulSoup

business_insider_link = (
    "https://markets.businessinsider.com/index/components/s&p_500?p={}"
)
base_link = "https://markets.businessinsider.com"
LINK = "http://www.cbr.ru/scripts/XML_daily.asp"

PAGES = range(1, 12)


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.content.read()


async def fetch_page(url, session):
    html = await fetch(session, url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", attrs={"class": "table table-small"})
    headers, *raw_companies, footers = table.find_all("tr")
    companies = list()
    for raw_company in raw_companies:
        raw_info, *trash, year_change, footer = raw_company.find_all("td")
        info = raw_info.find("a")
        year_change = year_change.find_all("span")

        company_info = {
            "link": urljoin(base_link, info["href"]),
            "abbr": info["href"].split("/")[-1].split("-")[0].upper(),
            "year_growth": float(year_change[1].get_text().strip("%")),
        }
        await parse_company_page(session, company_info)

        companies.append(company_info)

    return companies


async def fetch_all(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        company_list_pages = [business_insider_link.format(p) for p in PAGES]
        tasks = [fetch_page(url, session) for url in company_list_pages]
        usd_rate, *companies = await asyncio.gather(get_usd_rate(session), *tasks)
    companies = [item for sublist in companies for item in sublist]
    return usd_rate, companies


async def get_usd_rate(session):
    xml = await fetch(session, LINK)

    soup = BeautifulSoup(xml, "xml")
    for valute in soup.find_all("Valute"):
        if valute.find("CharCode").get_text() == "USD":
            return float(valute.find("Value").get_text().replace(",", "."))


async def parse_company_page(session, company):
    html = await fetch(session, company["link"])
    soup = BeautifulSoup(html, "html.parser")

    name_raw = (
        soup.find("div", attrs={"class": "price-section__row"}).find("span").get_text()
    )
    company["name"] = name_raw.strip()

    price_raw = (
        soup.find("div", attrs={"class": "price-section__values"})
        .find("span")
        .get_text()
        .replace(",", "")
    )
    company["price"] = float(price_raw)

    div = soup.find("div", attrs={"class": "snapshot"})
    try:
        pe_ratio_raw = div.find(
            "div", text="P/E Ratio", attrs={"class": "snapshot__header"}
        ).parent.get_text()
        company["pe_ratio"] = float(
            pe_ratio_raw.strip().split("\n")[0].strip().replace(",", "")
        )
    except AttributeError:
        company["pe_ratio"] = float("inf")

    script = div.find("script").string
    script = script.split("\n")
    low_price_row = [
        row.strip() for row in script if row.strip().startswith("low52weeks")
    ][0]
    high_price_row = [
        row.strip() for row in script if row.strip().startswith("high52weeks")
    ][0]
    low_price = float(low_price_row.split(":")[-1].replace(",", ""))
    high_price = float(high_price_row.split(":")[-1].replace(",", ""))
    company["weekly_growth"] = round((high_price - low_price) / low_price * 100, 2)


def make_top_10_json(filename, companies, keyword, sort_func, desc):
    top_10_companies = sorted(companies, key=sort_func, reverse=desc)[:10]
    top_10_companies = [
        {"name": c["name"], "abbr": c["abbr"], keyword: c[keyword]}
        for c in top_10_companies
    ]

    with open(filename, "w") as f:
        json.dump(top_10_companies, f, indent=2)


if __name__ == "__main__":
    start = datetime.datetime.now()
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(fetch_all(loop))
    usd_rate = results[0]
    companies = results[1]
    for c in companies:
        c["price"] = round(c["price"] * usd_rate, 2)
        c["weekly_growth"] = round(c["weekly_growth"] * usd_rate, 2)

    make_top_10_json(
        filename="top_10_price.json",
        companies=companies,
        keyword="price",
        sort_func=lambda x: x["price"],
        desc=True,
    )

    make_top_10_json(
        filename="top_10_pe.json",
        companies=companies,
        keyword="pe_ratio",
        sort_func=lambda x: x["pe_ratio"],
        desc=False,
    )

    make_top_10_json(
        filename="top_10_year_growth.json",
        companies=companies,
        keyword="year_growth",
        sort_func=lambda x: x["year_growth"],
        desc=True,
    )

    make_top_10_json(
        filename="top_10_weekly_growth.json",
        companies=companies,
        keyword="weekly_growth",
        sort_func=lambda x: x["weekly_growth"],
        desc=True,
    )

    print(f"It took: {(datetime.datetime.now() - start).seconds}s")
