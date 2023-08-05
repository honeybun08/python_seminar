# В списке целых чисел оставить только двузначные

my_list = [1, 55, 3, 26, 685, 999, 7774, 2, 77, 10, 99, 100, 0]
res = list(filter(lambda x: 9<x<100, my_list))
print(res)

# 2й вариант
# list_1 = [1, -13, -2, 45, -100, 664, 56]
# num_array = list(filter(lambda x: 10 <= abs(x) <= 99, list_1))
# print(num_array)














# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)


# def same_by(characteristic, objects):
#     counter = [1 for i in objects if i % 2 == 0]
#     if sum(counter) == len(objects): return True
#     else: return False

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values): print('same')
# else: print('different')