# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
try:
    n = int(input('Введите день недели: '))
    if n == 6 or n == 7:
        print('Сегодня выходной')
    elif n > 7 or n < 1:
        print('Такого дня недели не существует')
    else:
        print('Сегодня рабочий день')
except:
    print('Некорректно введены данные!')