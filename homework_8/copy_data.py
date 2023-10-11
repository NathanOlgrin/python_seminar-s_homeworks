from print_data import print_file
from return_data_file import data_file


def copy_file():
    print_file()
    nf_copy = int(input("Какой файл вы хотите копировать?"))
    while nf_copy < 1 or nf_copy > 2 :
        nf_copy = int(input("Ошибка! Такого файла нет! Какой файл вы хотите копировать?"))
    nf_paste = int(input("В какой файл вы хотите копировать?"))
    while nf_paste < 1 or nf_paste > 2 or nf_paste == nf_copy:
        nf_paste = int(input("Ошибка! В этот файл копировать нельзя! Какой файл вы хотите копировать?"))
    with open(f'db/data_{nf_copy}.txt', 'r', encoding='utf-8') as file:
        data_copy = file.readlines()
    with open(f'db/data_{nf_paste}.txt', 'r', encoding='utf-8') as file:
        data_paste = file.readlines()
    choice_copy = int(input("Вы хотите скопировать одну строку или полностью файл? \n"
                            "1. Одну строку\n"
                            "2. Полностью файл"))
    while choice_copy < 1 or choice_copy > 2:
        choice_copy = int(input("Ошибка! Выберите один из двух предложенных вариантов: \n"
                                "1. Скопировать одну строку\n"
                                "2. Скопировать полностью файл"))
    if choice_copy == 1 :
        number_row_copy = int(input("Какую строку вы хотите скопировать?"))
        while number_row_copy < 1 or number_row_copy > len(data_copy) :
            number_row_copy = int(input("Ошибка! Такой строки нет!\n"
                                      "Какую строку вы хотите скопировать? "))
        number_row_copy = number_row_copy - 1
        data_paste = data_paste + [data_copy[number_row_copy]]
        data_paste = ([f'{i + 1};{data_paste[i].split(";")[1]};{data_paste[i].split(";")[2]};{data_paste[i].split(";")[3]};{data_paste[i].split(";")[4]}' for i in range(len(data_paste))])
        with open(f'db/data_{nf_paste}.txt', 'w', encoding='utf-8') as file:
            file.writelines(data_paste)
        print("Данные скопированы!")

    else:
        for i in range (0, len(data_copy)):
            data_paste = data_paste + [data_copy[i]]
        data_paste = ([f'{i + 1};{data_paste[i].split(";")[1]};{data_paste[i].split(";")[2]};{data_paste[i].split(";")[3]};{data_paste[i].split(";")[4]}' for i in range(len(data_paste))])
        with open(f'db/data_{nf_paste}.txt', 'w', encoding='utf-8') as file:
            file.writelines(data_paste)
        print("Данные скопированы!")