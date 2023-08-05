# 1) Дан список, вывести в отдельном списке буквы, а в другом цифры, используя фильтр.
# ["asd", 1, 2, "gfd"]
# ["asd", "gfd"][1,2]

list_1 = ["asd", 1, 2, "gfd"]

list_res_letters = list(filter(lambda x: type(x)==str, list_1))
print(list_res_letters)

list_res_numbers = list(filter(lambda x: type(x)==int, list_1))
print(list_res_numbers)



# 2й вариант
# arr_in = input('Введите строку -> ').split()
# arr_1 = list(filter(lambda x: x.isdigit(), arr_in))
# arr_2 = list(filter(lambda x: x.isalpha(), arr_in))
# print(arr_1, arr_2)





# Задача №47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
# Пример ввода и вывода данных представлены на следующем
# слайде
# Задача №47. Решение в группах
# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)
# Вывод:
# ok
 
# def transformation(values):
#     return lambda x: x

# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(transformation(values), values))
# if values == transformed_values: print('OK') 
# else: print('FAIL')


# Или

# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(lambda x: x, values))
# if values == transformed_values: print('OK') 
# else: print('FAIL')




# объясняшка с урока

# def f(n):
#     return n**2

# def f1(n):
#     return n%2 == 0


# pre_arr = input().split()
# print(pre_arr)
# pre_arr = list(map(int, pre_arr))
# # # arr = list(map(f, pre_arr))
# # arr = list(map(lambda x: x**2, pre_arr))
# # print(arr)

# arr = list(filter(f1, pre_arr))
# print(arr)

# arr1= [1, 2, 3, 4, 5]
# arr2= [11, 22, 33, 44, 55, 66]


# arr3 = list(zip(arr1, arr2))
# arr3.append("asfsadf")
# print(arr3)


# arr = [11, 22, 33, 44, 55, 66]
# arr_res = list(enumerate(arr))
# print(arr_res)


