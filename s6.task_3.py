# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:           Вывод:
# 1 2 3 2 3       2

# string = input('Введите элементы списка через пробел -> ').split()
# dict = {}
# for i in string:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1

# count = 0
# for key, value in dict.items():
#     count += (value//2)   
# print(f'Код нашел - {count} пар в вашем списке!')



def task043():
    l = int(input("Введите длину списка: "))
    list_m = list_creator(l)
    print(counter(list_m))


def list_creator(x):
    my_list = []
    for i in range(0, x):
        my_list.append(int(input(f"Введите элемент списка из {x} элементов: ")))
    return my_list


def counter(my_list):
    counter = 0
    for i in range(len(my_list)):
        for j in range (i+1, len(my_list)):
            if my_list[i] == my_list[j]:
                counter+=1
    return counter

task043()


