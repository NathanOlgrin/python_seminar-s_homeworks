#Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.

try:
    n = int(input('Введите число: '))
    string_n=''
    while n !=1:
        z = n//2
        string_n+=str(n-(z*2))
        n=z
    string_n+=str(n)
    string_n = string_n[::-1]
    print(string_n)
except:
    print('Некорректно введены данные!')