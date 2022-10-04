#Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

from itertools import count


lst = ['one', 'two', 'onem', 'one', 'two', 'one']
a = 'onem'
def check_list(lst, a):
    count = 0
    for i in range(len(lst)):
        if lst[i] == a:
            count += 1
            if count == 2:
                return i
    else:
        return 'строки нет'


print(f"ответ: {check_list(lst, a)}")