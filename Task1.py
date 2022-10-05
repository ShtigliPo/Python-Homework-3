# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def sumOfuneven(mass):
    count = 0
    for i in range(1,len(mass),2):
        count += mass[i]
    print(count)
a = [random.randint(1, 10) for i in range(5)]
print(a)
sumOfuneven(a)
