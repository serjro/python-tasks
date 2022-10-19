# 3  Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random
mas=[round(random.uniform(0,10),2) for _ in range(10)]
part=[round(i-int(i),2) for i in mas]
print(mas,'\nmax:',max(part),'\nmin:',min(part),'\ndif:',max(part)-min(part))