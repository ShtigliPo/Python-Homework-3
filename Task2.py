# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def sumofpairs(mass):
    resmass = []
    if len(mass) % 2 == 0:
        for i in range(len(mass)//2):
            resmass.append(mass[i]*mass[len(mass)-1-i])
    else:
        for i in range(len(mass)//2+1):
            resmass.append(mass[i]*mass[len(mass)-1-i])
    print(resmass)
a = [random.randint(1,10) for i in range(5)]
print(a)
sumofpairs(a)