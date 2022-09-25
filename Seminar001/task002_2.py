#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
import os
clear = lambda: os.system('cls')
clear()
numbers = [2,10,15,2510,3010]
max_element = max(numbers)
print(max_element)