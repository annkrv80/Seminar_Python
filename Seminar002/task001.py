#Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все совпадают),
#2(если два совпадает) или 0 (если все числа различны).

a = int (input('1 '))
b = int (input('2 '))
c = int (input('3 '))
ar = [a,b,c]
count = [0,0,0]
for i in range(3):
    for j in range(3):
       if ar[i] == ar[j]:
        count[i]+=1
k = max(count)
if k == 1: 
    print(0)
else: 
    print(k)
