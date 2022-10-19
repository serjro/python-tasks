# 5  Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k=int(input('N='))
fib=(lambda a:lambda v:a(a,v))(lambda s,x:
        1 if x==-1 else 
        -1 if x==-2 else 
        s(s,x+2)-s(s,x+1) if x<0 else 
        s(s,x-2)+s(s,x-1) if x>0 else 0)
print([fib(m) for m in range(-k,k+1)])