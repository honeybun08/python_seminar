# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# Вывод:
# 3 3 2 12
#(каждое число вводится с новой строки)

n = int(input('Введите кол-во элементов первого множества: '))
first_list = [input('Введите элемент 1 списка: ') for i in range(0,n) if i < n]

m = int(input('Введите кол-во элементов второго множества: '))
second_list = [input('Введите элемент 2 списка: ') for j in range(0,n) if j < m]

# first_list = [3, 1, 3, 4, 2, 4, 12]
# second_list = [4, 15, 43, 1, 15, 1]

result = [i for i in first_list if i not in second_list] # через list comprehension
print(result)



# def task029():
#     m = int(input("Введите длину списка m: "))
#     n = int(input("Введите длину списка n: "))
#     list_m = list_creator(m)
#     list_n =list_creator(n)
#     res_list = set_from_list(list_m, list_n)
#     print(*res_list)

# def list_creator(x):
#     my_list = []
#     for i in range(0, x):
#         my_list.append(int(input(f"Введите элемент списка из {x} элементов: ")))
#     return my_list

# def set_from_list(list_m, list_n):
#     my_list = [list_m[i] for i in range(len(list_m)) if list_m[i] not in list_n]
#     return my_list

# task029()