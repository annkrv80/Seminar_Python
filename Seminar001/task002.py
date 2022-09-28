#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
import os
clear = lambda: os.system('cls')
clear()
a = int(input('Введите число a:'))
b = int(input('Bведите число b:'))
c = int(input ('Введите число с:'))
d = int(input ('Bведите число d:'))
e = int(input ('Bведите число e:'))
max=a
if b>max:
   max=b
if c>max:
   max=c
if d>max:
   max=d
if e>max:
    max=e
print(max)