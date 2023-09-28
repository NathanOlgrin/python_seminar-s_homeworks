# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов первого множества '))
m = int(input('Ведите количество элементов второго множества '))

set_n = set()
set_m = set()

for i in range(n):
    set_n.add(int(input('Введите элемент первого множества ')))

for i in range(m):
    set_m.add(int(input('Введите элемент второго множества ')))

# intermidate_set = set_n.intersection(set_m)
result = list(set_n.intersection(set_m))
for i in range (0, len(result)-1):
    for j in range (1, len(result)):
        if result[i]>result[j]:
            result[i], result[j] = result[j], result[i]
            
print(result)