# 3  Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
mas=[random.randint(1,9) for _ in range(10)]
ell=[i for i in mas if mas.count(i)==1]
print("Массив:",mas)
print("Неповторяющиеся элементы:",ell)