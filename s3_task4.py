# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


# # 1 Вариант строго по тз

# array = []
# # [0, -1, 5, 2, 3]

# while True:
#     n = int(input('Введите длину списка -> '))
#     if n > 0:
#         j = 1
#         while j <= n:
#             array.append(int(input(f'Введите {j} элемент массива -> ')))
#             j += 1
#         break

# print(array)
# count = 0
# frst = array[0]
# scnd = array[1]

# for i in range(0, len(array)):
#     if frst < scnd:
#         count += 1
#     frst, scnd = scnd, array[i]

# print(count)

list = [1,1,1,2,4,6,8,1,1,2]

count = 0
min_value = list[0]

for i in list:
    if i > min_value: count += 1
        # count += 1
    min_value = i # т.к. все дело в i

print(count)

# spisok = [4,3,5,6,1,2]
# chislo = [[spisok[i-1],spisok[i]] for i in range(1, len(spisok)) if spisok[i] > spisok[i-1]]
# chislo2 = [print(' (' + str(item[0]) + ' < ' + str(item[1]) + ') ') for item in chislo]
# print(chislo2)
    
