"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50
order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""
import types
from typing import Callable


class Order:
    def __init__(self, price, discount_func: Callable = None) -> None:
        self.price = price
        if discount_func is not None:
            self.final_price = types.MethodType(discount_func, self)

    def final_price(self):
        return self.price


def morning_discount(order):
    order.discount = 0.5
    return order.price - order.price * order.discount


def elder_discount(order):
    order.discount = 0.9
    return order.price - order.price * order.discount


if __name__ == "__main__":
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10
