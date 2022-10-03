#Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
from datetime import datetime


a = int(input('Введите размерность '))


def k():
    return (datetime.now().microsecond)


res = int(k()/10**a)
print(res)
