#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Products:
    """
    Класс, хранящий введенные значения в полях first и second
    """

    def __init__(self, first=0, second=0):
        """
        Конструктор класса, принимает два параметра, валидирует их и сохраняет в поля
        """
        if not isinstance(second, int):
            raise TypeError("Значение second должно быть целым числом")

        if first < 0 or second < 0:
            raise ValueError()

        self.__first = first
        self.__second = second

    def read(self, prompt=None):
        """
        Статичный метод для создания экземпляра класса
        """
        line = input() if prompt is None else input(prompt)
        parts = list(map(float, line.split(" ", maxsplit=1)))

        self.__first = float(parts[0])
        self.__second = int(parts[1])

        if parts[1] == 0:
            raise ValueError()

    def display(self):
        """
        Метод вывода на консоль результатов
        """
        print(f"Стоимость товара: {self.cost()}")

    def cost(self):
        """
        Метод возвращает стоимость товаров
        """
        return self.__first * self.__second


# Возвращение структуры требуемого типа
def make_products(first, second):
    return Products(first, second)


if __name__ == "__main__":
    prod = Products()
    prod.read("Введите цену и количество товара через пробел: ")
    prod.display()
