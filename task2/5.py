5. Реализуйте алгоритм перемешивания списка.

mas=[i for i in range(10)]
print('Массив:',mas)

# Вар.1
import random
mas_shaf=mas
random.shuffle(mas_shaf)
print('Перемешивание_1:',mas_shaf)

# Вар.2
mas_shaf=mas
for i in range(len(mas_shaf)):
    rnd = random.randint(0, len(mas_shaf) - 1)
    t = mas_shaf[i]
    mas_shaf[i] = mas_shaf[rnd]
    mas_shaf[rnd] = t
print('Перемешивание_2:',mas_shaf)