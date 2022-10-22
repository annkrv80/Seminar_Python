#Дан список, вывести отдельно буквы и цифры.
list=['1','a','li','25']
print([i for i in list if i.isdigit()])
print([i for i in list if i.isalpha()])