#Напишите программу, которая принимает на вход два числа и проверяет,
#является ли одно число квадратом другого.
a = int(input('Введите число а:'))
b = int(input('Введите число b:'))
if a**2==b:
    print('Yes')
elif b**2==a:
    print('Yes')
else:
    print('No')