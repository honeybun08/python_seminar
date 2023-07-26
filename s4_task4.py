# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
import re

string = re.split(' |\\.', input('Введите текст -> ').lower()) # для специфицких знаков
string.sort()
dict = {}
for i in string:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)
max_val = 0
max_key = ''
for key, value in dict.items(): # картеж
    if value > max_val:
        max_val = value
        max_key = key
print(f'Слово которое чаще всего встречалось - {max_key}, оно встретилось - {max_val} раз/раза!' )