# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой. Нельзя юзать find или count.

string1 = input('Введите, где ищем: ')
string2 = input('Введите, что ищем: ')

l2 = len(string2)
count=0
for i in range(0,len(string1)-l2+1):
    temp = string1[i:i+l2]
    if(temp==string2): count+=1
print(count)