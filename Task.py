#Преобразовать набор списков (используя функцию zip)
from itertools import zip_longest


users = ['user1','user2','user3','user4','user5']
ids = [4, 5, 9, 14, 7] 
salary = [111,222,333]
temp=[list(i)for i in zip(users,ids,salary)]
print(temp)
print(list(zip(*temp)))
temp1=[list(i) for i in zip_longest(users,ids,salary,fillvalue='')]
for i in range(len(temp1)):
    temp1[i]=list(filter(lambda x: x,temp1[i]))
print(temp1)
print(list(zip_longest(*temp1,fillvalue='')))