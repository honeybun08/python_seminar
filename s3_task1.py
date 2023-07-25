#  ВАРИАНТ 1 (ВЫБОР РУЧНОГО ИЛИ АВТОМАТИЧЕСКОГО РЕЖИМА)
# import random
#
# array_frs = []
# # Пользователь выбирает вручную или автоматически
# while True:
#     a = input('Как вы хотите заполнить список. Напишите (вручную или автоматически) -> ')
#     if a == 'вручную':
#         break
#     if a == 'автоматически':
#         break
#
# while True:
#     array_len = int(input('Введите длину списка -> '))
#     if array_len > 0:
#         break
#
# # Заполнение списка
# if a == 'вручную':
#     i = 1
#     while i <= array_len:
#         a = int(input(f'Введите {i} элемент списка -> '))
#         array_frs.append(a)
#         i += 1
# if a == 'автоматически':
#     while array_len > 0:
#         a = random.randint(-20, 20)
#         array_frs.append(a)
#         array_len -= 1
#
# print(array_frs)
#
# array_scnd = []
# count = 0
#
# # Метод подсчета уникальных знаков
# for i in array_frs:
#     if i not in array_scnd:
#         count += 1
#         array_scnd.append(i)
#
# print(f'В списке {count} различных чисел')

# ВАРИАНТ 2 (Элегантное решение в 1 строчку)
# print(len(set(input('Введите элементы списка через пробел').split())))

# ВАРИАНТ 3 (Лист дан или пользователь сам вводит)

# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# array = []
# # [1, 1, 2, 0, -1, 3, 4, 4]
# while True:
#     n = int(input('Введите длину списка -> '))
#     if n > 0:
#         j = 1
#         while j <= n:
#             array.append(int(input(f'Введите {j} элемент массива -> ')))
#             j += 1
#         break

# second_arr = []
# count = 0

# for i in array:
#     if i not in second_arr:
#         count += 1
#         second_arr.append(i)

# print(f'В списке {count} различных чисел')

# или
list_1 = [1, 1, 2, 3, 4, 6, 2, 5]
mnoj = set(list_1)

print(mnoj)

