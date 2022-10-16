4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n=6
m=1
mas=[x for x in range(-n,n+1)]
f = open("file.txt", "r")
idx = [int(x.strip()) for x in f.readlines()]
f.close
print('Массив:',*mas,'\nСодержимое файла:',*idx,'\nЭлементы:',end='')
for el in idx:
    m *= mas[el]
    print(mas[el],end=' ')
print('\nПроизведение:',m)