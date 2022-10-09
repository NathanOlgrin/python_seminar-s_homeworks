# Напишите простой калькулятор, который считывает с пользовательского
# ввода три строки: первое число, второе число и операцию, после чего
# применяет операцию к введённым числам ("первое число" "операция"
# "второе число") и выводит результат на экран.

try:
    first_number = float(input('Введите первое число: '))
    second_number = float(input('Введите второе число: '))
    operation = input('Введите операцию: ')
    match operation.split():
        case ["+"]: print(first_number+second_number)
        case ["-"]: print(first_number-second_number)
        case ["/"]: 
            if second_number!= 0 :
                print(first_number/second_number)
            else:
                print('Деление на 0!')
        case ["*"]: print(first_number*second_number)
        case ["mod"]: print(first_number%second_number)
        case ["pow"]: print(first_number**second_number)
        case ["div"]: print(first_number//second_number)
except:
    print('Некорректно введены данные!')