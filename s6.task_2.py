# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: 5
# 1 2 3 4 5
# Вывод: 0
# Ввод: 5 
#  1 5 1 5 1
# Вывод: 2
# (каждое число вводится с новой строки)

# 1 вариант
# while True:
#     n = int(input('Введите кол-во элементов множества -> '))
#     if n > 0:
#         break

# while True:
#     array = input('Введите элементы массива через пробел -> ').split()
#     if len(array) == n:
#         break

# count = 0
# for i in range(2, len(array)):
#     if array[i - 2] < array[i - 1] and array[i] < array[i - 1]:
#         count += 1

# print(count)



def task30():
    list_new = [1, 2, 3, 4, 5]
    print(find_between_less_elements(list_new))

def find_between_less_elements(my_list):
    count = 0
    for i in range(1,len(my_list)-1):
        if my_list[i-1]<my_list[i]>my_list[i+1]:
            count +=1
    return count

task30()



# n = int(input('Введите кол-во элементов множества -> '))
# arr = [input('Введите элемент массива -> ') for i in range(0, n)]
# res = [1 for i in range(0,len(arr)) if arr[i - 2] < arr[i - 1] and arr[i] < arr[i - 1]]
# print(sum(res))