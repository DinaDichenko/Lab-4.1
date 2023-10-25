#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Products:
    def __init__(self, a=0, b=0):
        a = float(a)
        b = int(b)

        if a < 0 or b < 0:
            raise ValueError()

        self.__first = a
        self.__second = b

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    # Прочитать значения first и second. Значения вводятся через пробел
    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(float, line.split(" ", maxsplit=1)))

        self.__first = float(parts[0])
        self.__second = int(parts[1])

        if parts[1] == 0:
            raise ValueError()

    # Вывод на экран
    def display(self):
        print(f"Стоимость товара: {self.cost()}")

    # Вычисление стоимости товара
    def cost(self):
        return self.__first * self.__second


# Возвращение структуры требуемого типа
def make_exp(first, second):
    return Products(first, second)


if __name__ == "__main__":
    prod = Products()
    prod.read("Введите цену и количество товара через пробел: ")
    prod.display()
