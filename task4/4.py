# 4  Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random
indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079"
           }

def degree(deg,reverse=False): # получение символов степени
    index=indexes if not reverse else {v:k for k, v in indexes.items()} # меняем местами кл/зн в словаре при reverse
    return "".join(str(index[char] or "") for char in str(deg)) # заменяем вх значения по словарю

k=7 # степень
members=[] # члены
for i in range(k,-1,-1):
    m=str(random.randint(0,100))
    m=''if m=='0' else 'x' if  m=='1' else m+'x' # создаем коэф.
    if m!='':
        # создаем степень
        members.append(m+degree(i) if i>1 else str(m) if i==1 else str(m)[:-1] if m!='x' else '1')
s=' + '.join(members)+' = 0'

f = open('files\\task_4-4.txt', 'w', encoding="utf-8")
f.write(s)
f.close()
print(s)