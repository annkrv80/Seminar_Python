#Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
lst = [1,2,0,5,6,8,4,1,10]
for i in range(1,len(lst)):
    if lst[i]>lst[i-1]:
        print(lst[i],end=" ")