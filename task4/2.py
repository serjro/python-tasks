# 2  Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n=84
m=[]
while n!=1:
    j=2
    while n%j!=0:
        j+=1
    m.append(j)
    n=n/j
print(m)      