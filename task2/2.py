# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n=int(input('N='))
f1=lambda a:lambda v:a(a,v)
f2=(f1)(lambda s,x:1 if x==0 else x*s(s,x-1))
print([f2(m+1) for m in range(n)])
