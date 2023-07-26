# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

string = input('Введите элементы списка через пробел -> ').split()
dict = {}
res = ''
for i in string:
    if i in dict:
        dict[i] += 1
        res += str(i) + '_'+ str(dict[i]) + ' ' # значение буквы _ количество использования + пробел
    else:
        dict[i] = 0
        res += str(i) + ' ' # по факту значение буквы _ 0 (0=ничего)
print(dict)
print(res)

# 2й вариант
string = input('Введите элементы списка через пробел -> ').split()

dict = {}
result = ''
for i in string:
    if i not in dict:
        dict[i] = 0
        result += str(i) + ' '
    else:
        dict[i] += 1
        result += str(i) + '_' + str(dict[i]) + ' '
print(dict)
print(result)