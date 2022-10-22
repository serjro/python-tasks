# 5  Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from collections import Counter # перевод словаря в коллекцию, чтобы потом сложить их
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

def sub(s): # разложение строки многочлена в словарь
    a={}
    for i in s[:-4].split(' + '):
        if ('x' in i):
            a[1 if len(i.split('x')[1])==0 else int(degree(i.split('x')[1],1))]=int(i.split('x')[0])
        else:
            a[0]=int(i)
    return a # получаем словарь, где ключ-степень, значение-коэф.

def sum_dict(a1,a2): # суммирование словарей многочленов
    for i in a2.keys():
        if i in a1.keys():
            a1[i]=a1[i]+a2[i]
        else:
            a1[i]=a2[i]
    return a1

# ss после загрузки из файлов. Закомментировать загрузку чтобы не создавать файлы
# ss = ['94x⁵ + 18x³ + 28x² + 23x + 2 = 0', '11x⁷ + 88x⁵ + 38x⁴ + 19x³ + 44x² + 10x + 38 = 0']

ss=[] # загружаем файлы
for i in ['files\\task_4-5_f1.txt','files\\task_4-5_f2.txt']:
    f = open(i, 'r', encoding="utf-8")
    ss += [f.readline()]
    f.close()
print('Многочлен_1:',ss[0],'\nМногочлен_2:',ss[1])

ss=[i.replace(' - ',' + -') for i in ss]

#mbr = Counter(sub(ss[0])) + Counter(sub(ss[1])) Проще, но теряются отрицательные значения в словаре
mbr = sum_dict(sub(ss[0]),sub(ss[1]))
members=[] # члены 
for i in sorted(mbr.keys(),reverse=1): # далее собираем многочлен по ключам-i
    m=str(mbr[i]) # создаем коэф.
    m='' if m=='0' else 'x' if  m=='1' else '-x' if  m=='-1' else m+'x' # пропускаем 0, 1 коэф
    if m!='': # создаем степень
        members.append(m+degree(i) if i>1 else str(m) if i==1 else str(m)[:-1] if m!='x' else '1')# пропускаем 0,1,x в степ
s=' + '.join(members)+' = 0'
s=s.replace('+ -','- ') if '+ -' in s else s # доводка отриц.значений
print('Сумма:',s)