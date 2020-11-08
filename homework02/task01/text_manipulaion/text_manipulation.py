"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from string import punctuation
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    unique_words = dict()
    with open(file_path) as fi:
        for line in fi:
            for word in line.split():
                word = (
                    word.encode()
                    .decode("unicode-escape")
                    .strip('!"#$%&()*+,-./:;<=>?@[]^_`{|}~')
                )
                unique_chars = set(word)
                unique_chars_amount = len(unique_chars)
                if unique_chars_amount in unique_words:
                    unique_words[unique_chars_amount].append(word)
                    if len(unique_words[unique_chars_amount]) > 10:
                        unique_words[unique_chars_amount].sort(key=len)
                        unique_words[unique_chars_amount] = unique_words[
                            unique_chars_amount
                        ][:10]
                else:
                    unique_words[unique_chars_amount] = [
                        word,
                    ]

            unique_amount = list(unique_words.keys())
            if len(unique_amount) > 10:
                unique_amount.sort(reverse=True)
                for key in unique_amount[10:]:
                    unique_words.pop(key)

        result = list()
        for amount in sorted(list(unique_words.keys()), reverse=True):
            for word in unique_words[amount]:
                result.append(word)
                if len(result) == 10:
                    return sorted(result, key=len, reverse=True)
        return sorted(result, key=len, reverse=True)


def get_rarest_char(file_path: str) -> str:
    chars_dict = {}
    with open(file_path, "r") as fi:
        for line in fi:
            for c in line:
                if c not in chars_dict:
                    chars_dict[c] = 1
                else:
                    chars_dict[c] += 1
    res = min(chars_dict, key=chars_dict.get)
    return res


def count_punctuation_chars(file_path: str) -> int:
    counter = 0
    with open(file_path, "r") as fi:
        for line in fi:
            for c in line:
                if c in punctuation:
                    counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    counter = 0
    with open(file_path, "r") as fi:
        for line in fi:
            for c in line:
                if not c.isascii():
                    counter += 1
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    chars_dict = {}
    with open(file_path, "r") as fi:
        for line in fi:
            for c in line:
                if not c.isascii():
                    if c not in chars_dict:
                        chars_dict[c] = 1
                    else:
                        chars_dict[c] += 1
    res = max(chars_dict, key=chars_dict.get)
    return res
