# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число: '))
list=[]
result=1
for i in range(1,n+1):
    result=result*i
    list.append(result)
print(list)