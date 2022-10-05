# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def fl(n):
    res = str(n)
    fif = res.find('.')
    res = float('0.' + res[fif+1::])
    return res


def difoffloat(mass):
    res = []

    for i in mass:
        res.append(fl(i))
    print(max(res)-min(res))


a = [1.19, 1.28, 3.16, 5.25, 10.01]
print(a)
difoffloat(a)
