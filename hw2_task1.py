# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int(input('Введите количество монет: '))
eagle = 0
tails = 0
for i in range(n): #проход каждого i в кол-ве монеток
    num = int(input('Если монетка с орлом - введите (1), если с решкой - (0): '))
    if num == 1:
        eagle += 1
    else:
        tails += 1
if eagle < tails:
    print(f'Переверните {eagle} монет ')
elif eagle == tails:
    print(f'Количество монеток орлов и решек одинаково, по {tails} штук')
else:
    print((f'Переверните {tails} монет'))

