# 1  Вычислить число c заданной точностью d

import math
d=.0001
num=math.pi
acc=len(str(d).split('.')[1])
print("Число:",num)
print("Точность:",acc)
print("Результат:",round(num,acc))