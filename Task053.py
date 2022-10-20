#Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет,
#можно ли из этих отрезков составить треугольник. 
a=int(input())
b=int(input())
c=int(input())

def triangle(x,y,z):
    flag = False
    if x+y>z and x+z>y and y+z>x:
        flag=True
    return 'YES' if flag else 'NO'

print(triangle(a,b,c))
    