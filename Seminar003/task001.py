#Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
#Элементы нужно выводить в том порядке, в котором они встречаются в списке.

from itertools import count


lst = [1, 2, 2, 3, 4, 4, 5]
lst2 = []
count = 0
for i in lst:
    for j in lst:
        if i == j:
            count += 1
    if count == 1:
        lst2.append(i)
    count = 0
print(lst2)
