#Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
#Найдите количество и выведите его.

#Пример:
#list_1 = [1, 2, 3, 4, 5]
#k = 3
# 1

# # 1й вариант
# list_1 = []

# while True:
#     n = int(input('Введите длину списка -> '))
#     if n > 0:
#         j = 1
#         while j <= n:
#             list_1.append(int(input(f'Введите {j} элемент массива -> ')))
#             j += 1
#         break

# print(list_1)


# k = (int(input('Введите число k:')))

# count_k = 0

# for i in list_1:
#     if i == k:
#         count_k +=1
#     i +=1

# print(count_k)

# 2й вариант
list = [1,2,3,4,4,5,5,7,2,6]
k = 1

count_k = 0

for i in list:
    if i == k:
        count_k +=1
    i +=1

print(count_k)
