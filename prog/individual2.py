#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class Angle:
    def __init__(self, a=0, b=0):
        a = float(a)
        b = float(b)

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

    # Выврд на экран
    def display(self):
        print(f"В радианах: {self.radian()}")
        print(f"В диапазоне 0-360: {self.diapazon()}")
        print(f"Синус: {self.sinus()}")
        print(f"Изменение на определенный угол: {self.change(prod3)}")
        print(f"Сравнение с другим углом: {self.comparison(prod2)}")

    # Перевод в радианы
    def radian(self):
        return math.radians(self.first + self.second / 60)

    # Приведение к диапазону 0-360
    def diapazon(self):
        grad = self.first + self.second / 60
        if (grad) > 360 or grad < 0:
            return grad % 360

        else:
            return grad

    # Получение синуса
    def sinus(self):
        return math.sin(self.radian())

    # Увеличение/уменьшение угла на заданную величину
    def change(self, other_angle):
        grad1 = self.first + self.second / 60
        grad2 = other_angle.first + other_angle.second / 60
        return grad1 + grad2

    # Сравнение углов
    def comparison(self, other_angle):
        grad1 = self.first + self.second / 60
        grad2 = other_angle.first + other_angle.second / 60

        if grad1 > grad2:
            return f"{grad1} больше {grad2}"

        else:
            if grad1 == grad2:
                return f"{grad1} равен {grad2}"

            else:
                return f"{grad1} меньше {grad2}"


if __name__ == "__main__":
    prod = Angle()
    prod.read("Введите угол(градусы и минуты вводятся через пробел): ")

    prod2 = Angle()
    prod2.read("Введите угол для сравнения: ")

    prod3 = Angle(30, 0)
    print(prod.comparison(prod2))
    prod.display()
