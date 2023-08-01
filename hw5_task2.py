# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.

# Пример:
# sum(2, 2)
# # 4

# def sum(a,b):
#     if b == 0:
#         return a
#     else:
#         return sum(a+1, b-1)

# a = 3
# b = 25
# print(sum(a,b))

def sum(a,b):
    if a == 0:
        return (b)
    else:
        return (sum(a - 1, b))
    
print(sum(a = 8, b = 4))