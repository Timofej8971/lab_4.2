#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Реализовать класс Rational, используя два списка из 100 элементов типа int для
представления числителя и знаменателя. Каждый элемент является десятичной цифрой.
Младшая цифра имеет меньший индекс (единицы — в нулевом элементе списка). Реальный
размер списка задается как аргумент конструктора инициализации.
'''


class Rational:

    def __init__(self, chisl, znam):
        self.list_chisl = []
        self.list_znam = []
        self.CONST_MAX_SIZE = 100
        self.num_chisl = str(chisl)
        self.num_znam = str(znam)
        if len(self.num_znam) and len(self.num_chisl) < self.CONST_MAX_SIZE:
            if chisl and znam is not None:
                for i in self.num_chisl:
                    self.list_chisl.append(i)
                for i in self.num_znam:
                    self.list_znam.append(i)
        else:
            raise ValueError()

    def size(self):
        return f'Размер числителя {len(self.list_chisl)},' \
               f' Размер знаминателя: {len(self.list_znam)}'

    def __getitem__(self, item):
            return f'Элемент в списке числителей {self.list_chisl[item]} \n' \
                   f'Эдемент в списке знаминателей {self.list_znam[item]}'


    def __setitem__(self, list_name, item, value):
        if list_name == 'chisl':
            self.list_chisl[item] = value
        elif list_name == 'znam':
            self.list_znam[item] = value
        else:
            raise ValueError()

    def __delitem__(self, list_name, item):
        if list_name == 'chisl':
            self.list_chisl.pop(item)
        elif list_name == 'znam':
            self.list_znam.pop(item)
        else:
            raise ValueError()

    def __add__(self, other):
        sum_list_chisl = []
        sum_list_znam = []
        if len(self.list_chisl) > len(other.list_chisl):
            for idx, i in self.list_chisl:
                if other.list_chisl is not None:
                    sum_list_chisl.append(int(self.list_chisl[int(idx)]) + int(other.list_chisl[int(idx)]))
                else:
                    sum_list_chisl.append(self.list_chisl[int(idx)])
        else:
            for idx, i in other.list_chisl:
                if self.list_chisl is not None:
                    sum_list_chisl.append(int(self.list_chisl[int(idx)]) + int(other.list_chisl[int(idx)]))
                else:
                    sum_list_chisl.append(other.list_chisl[int(idx)])

        if len(self.list_znam) > len(other.list_znam):
            for idx, i in self.list_znam:
                if other.list_znam is not None:
                    sum_list_znam.append(int(self.list_znam[int(idx)]) + int(other.list_znam[int(idx)]))
                else:
                    sum_list_znam.append(self.list_znam[int(idx)])
        else:
            for idx, i in other.list_znam:
                if self.list_znam is not None:
                    sum_list_znam.append(int(self.list_znam[int(idx)]) + int(other.list_znam[int(idx)]))
                else:
                    sum_list_znam.append(other.list_znam[int(idx)])
        return f'Сумма числителей {sum_list_chisl},' \
               f'Сумма знаминателей {sum_list_znam}'

    def __sub__(self, other):
        sub_list_chisl = []
        sub_list_znam = []
        if len(self.list_chisl) > other.list_chisl:
            for idx, i in self.list_chisl:
                if other.list_chisl is not None:
                    sub_list_chisl.append(int(self.list_chisl[int(idx)]) - int(other.list_chisl[int(idx)]))
                else:
                    sub_list_chisl.append(self.list_chisl[int(idx)])
        else:
            for idx, i in other.list_chisl:
                if self.list_chisl is not None:
                    sub_list_chisl.append(int(self.list_chisl[int(idx)]) - int(other.list_chisl[int(idx)]))
                else:
                    sub_list_chisl.append(other.list_chisl[int(idx)])

        if len(self.list_znam) > other.list_znam:
            for idx, i in self.list_znam:
                if other.list_znam is not None:
                    sub_list_znam.append(int(self.list_znam[int(idx)]) + int(other.list_znam[int(i)]))
                else:
                    sub_list_znam.append(self.list_znam[int(i)])
        else:
            for idx, i in other.list_znam:
                if self.list_znam is not None:
                    sub_list_znam.append(int(self.list_znam[int(idx)]) + int(other.list_znam[int(idx)]))
                else:
                    sub_list_znam.append(other.list_znam[int(idx)])
        return f'Сумма числителей {sub_list_chisl},' \
               f'Сумма знаминателей {sub_list_znam}'

if __name__ == '__main__':
    x = Rational(512, 512)
    y = Rational(611, 611)
    print(x[0])
    print(x.size())
    print(x+y)
    print(x-y)

