#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Поле first — дробное число, левая граница диапазона; поле second — дробное число,
правая граница диапазона. Реализовать метод rangecheck() — проверку заданного числа
на принадлежность диапазону.
'''


class MyClass:

    def __init__(self, chislo=0):
        self.chislo = chislo

    def __lt__(self, other):
        if self.chislo < other.chislo:
            return "done"


if __name__ == '__main__':
    first = MyClass(2)
    second = MyClass(7)
    third = MyClass(5)
    if first < second and second < third:
        print(f'Число {second} внутри диапазона от {first} до {third}')
