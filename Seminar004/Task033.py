#НОК
a = int(input('Введите число '))
b = int(input('Введите число '))
if a > b:
    num = a
else:
    num = b
trigger = True
while trigger == True:
    if (num % a) == 0 and (num % b) == 0:
        trigger == False
    else:
        num += 1
print(num)
