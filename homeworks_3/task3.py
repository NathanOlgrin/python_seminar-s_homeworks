#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
#и минимальным значением дробной части элементов.

from decimal import Decimal
import decimal

list = [1.1, 1.2, 3.1, 5, 10.01]
list_fractional = []
decimal.getcontext().prec = 12
for i in range(0,len(list)):    #цикл забивает список дробных частей начального списка
    if list[i]%1!=0:
        integer_part=int(list[i])
        fractional_part = Decimal(list[i]) - Decimal(integer_part)
        list_fractional.append(fractional_part)
max=0.0
min=1000.0
print(list_fractional)
for i in range(0,len(list_fractional)): #цикл поиска минимального и максимального значения
    if min>list_fractional[i]:
        min=list_fractional[i]
    if max<list_fractional[i]:
        max=list_fractional[i]
result = Decimal(max) - Decimal(min)
print(Decimal(result).normalize())