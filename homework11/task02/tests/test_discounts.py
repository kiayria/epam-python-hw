from discounts.discounts import Order, elder_discount, morning_discount

order_1 = Order(100)
order_2 = Order(100, morning_discount)
order_3 = Order(100, elder_discount)


def test_order_no_discount():
    assert order_1.final_price() == 100


def test_order_morning_discount():
    assert order_2.final_price() == 50


def test_order_elder_discount():
    assert order_3.final_price() == 10
