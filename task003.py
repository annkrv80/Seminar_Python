#Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
from random import randrange
from unittest import result


n = int (input('Введите число N '))

for i in range (n):
    result = randrange(-100,100)
    print(result,end=" ")


    