# Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

try:
    n = int(input("Введите размерность пространства: "))
    list1 = []
    for i in range(n):
        print(f'Введите {i+1} координату первой точки: ')
        list1.append(float(input()))
    list2 = []
    for i in range(n):
        print(f'Введите {i+1} координату второй точки: ')
        list2.append(float(input()))
    list3 = []
    result=0
    for i in range(n):
        list3.append((list2[i]-list1[i])**2)
        result+=list3[i]
    result = result**0.5
    print('Расстояние между точками равно: ', round(result,2))
except:
    print("Неправильно введены координаты")