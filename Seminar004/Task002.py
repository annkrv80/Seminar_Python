#Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
from re import A


a = int (input('Введите A '))
b = int (input('Введите B '))
c = int (input('Введите C '))
d= b**2-4*a*c
print(d)
if d<0:
    print('Корней нет')
elif d==0:
    x=-b/(2*a)
    print ('x=',x)
else:
    x1=round((-b+math.sqrt(d))/(2*a),2)
    x2=round((-b-math.sqrt(d))/(2*a),2)
    print('x1=',x1,'x2=',x2)

