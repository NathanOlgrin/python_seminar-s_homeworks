# Задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
try:
    x = float(input('Введите координату X:'))
    y = float(input('Введите координату Y:'))
    if x > 0 and y > 0:
        print('Точка расположена в 1 четверти')
    if x < 0 and y > 0:
        print('Точка расположена в 2 четверти')
    if x < 0 and y < 0:
        print('Точка расположена в 3 четверти')
    if x > 0 and y < 0:
        print('Точка расположена в 4 четверти')
except:
    print('Некорректно введены данные!')