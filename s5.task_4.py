# Задача №37. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def ReverseNums(n):
    if n == 0:
        return ""
    num = int(input('Введите число:'))
    return ReverseNums(n - 1) + f' {num}'

print(ReverseNums(4))



# def Reverse(num):
#     if num == 0:
#         return ""
#     number = input("Введите число: ")
#     return f"{Reverse(num-1)}{number} " #пробел в конце, потому что идём в обратную сторону
    

# n = int(input("Введите число N элементов: "))
# print(Reverse(n))



# def ReverseNumOrder(value):
#     n = int(input('Введите элемент: '))
#     if value > 1:
#         ReverseNumOrder(value - 1) # для многократного принта
#     print(n, end = ' ')

# ReverseNumOrder(int(input('Введите колличество элементов: ')))   