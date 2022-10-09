# Задайте двумерный массив из целых чисел.
# Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.

try:
    def fill_array(array):  # Заполнение начального массива с клавиатуры
        for i in range(len(array)):
            for j in range(len(array[i])):
                array[i][j] = int(input(f'Введите {i}{j}-й элемент массива: '))

    def fill_interim_array(array, interim_array):  # Заполнение промежуточного массива
        for i in range(len(array)):
            for j in range(len(array[i])):
                interim_array.append(array[i][j])

    def sort_interim_array(interim_array):  # Сортировка промежуточного массива
        for i in range(len(interim_array)):
            for j in range(len(interim_array) - i - 1):
                if interim_array[j] > interim_array[j + 1]:
                    temp = interim_array[j]
                    interim_array[j] = interim_array[j + 1]
                    interim_array[j + 1] = temp

    def sort_array(array, interim_array):  # Перезаполнение начального массива
        z = 0
        for i in range(len(array)):
            for j in range(len(array[i])):
                array[i][j] = interim_array[z]
                z += 1

    def print_array(array):  # Вывод массива на экран
        for i in range(len(array)):
            for j in range(len(array[i])):
                print(array[i][j], end=' ')
            print()


    line = int(input('Введите количество строк: '))
    column = int(input('Введите количество столбцов: '))
    array = [[0 for i in range(column)] for j in range(line)]
    fill_array(array)
    interim_array = []
    fill_interim_array(array, interim_array)
    sort_interim_array(interim_array)
    sort_array(array, interim_array)
    print_array(array)
except:
    print('Некорректно введены данные!')