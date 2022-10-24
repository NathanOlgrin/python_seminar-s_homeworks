# Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

from decimal import Decimal
import decimal

n = float(input('Введите число: '))
integer_part = int(n)
decimal.getcontext().prec=12
fractional_part = Decimal(n)-Decimal(integer_part)
print(integer_part)
print(fractional_part)
summ = 0
while(integer_part!=0):
    summ=summ+(integer_part%10)
    integer_part=integer_part//10
while (fractional_part!=0):
    summ=summ+int(fractional_part*10)
    fractional_part=Decimal(fractional_part*10-int(fractional_part*10))
print(summ)