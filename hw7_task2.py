# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y) 
#  1  2   3   4   5   6
#  2  4   6   8   10  12
#  3  6   9   12  15  18
#  4  8   12  16  20  24
#  5  10  15  20  25  30
#  6  12  18  24  30  36 

operation = str(input('Введите нужную операцию (+, -, *, /): '))
num_rows = int(input('Введите число рядов: '))
num_columns = int(input('Введите число столбцов: '))

def operation_table(operation):
    if operation == '+':
        return lambda x, y: (x - 1) + (y - 1)
    if operation == '-':
        return lambda x, y: x - y
    if operation == '*':
        return lambda x, y: x * y
    if operation == '/':
        return lambda x, y: round(x / y,2) # окргуление до 2х знаков

def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows + 1): # т.к. по условию счет от единицы(и доходим до самого конца кол-ва рядов и столбцов)
        for j in range(1, num_columns + 1):
            print(operation(i, j), end = ' ')
        print()

print_operation_table(operation_table(operation),num_rows,num_columns) 



