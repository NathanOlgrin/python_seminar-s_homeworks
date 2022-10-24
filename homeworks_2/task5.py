# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z .
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25, сами значения предикатов случайные, проверяем это утверждение 100 раз, 
# с помощью модуля time выводим на экран , сколько времени отработала программа.
import random
import time

start_time = time.time()
for i in range(1,101):
    n = random.randint(6,26)
    variable_list = []
    for j in range(0,n):
        variable_list.append(random.choice([True, False]))
    left_part = variable_list[0]
    right_part = variable_list[0]
    for j in range(0, n):
        left_part = left_part or variable_list[j]
        right_part = not right_part  and not variable_list[j]
    left_part = not left_part
    if left_part == right_part :
        print('Утверждение истинно для ', end = " ")
        for j in range(0,n):
            print(f'j[{j+1}]={variable_list[j]}', end = " ")
    print()
print("Программа работала ", time.time() - start_time, "секунд")