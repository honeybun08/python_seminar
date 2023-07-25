#Требуется найти в массиве list_1 самый близкий 
#по величине элемент к заданному числу k и вывести его.

#Пример:
#list_1 = [1, 2, 3, 4, 5]
#k = 6
#5

list_1 = [34, 15, 6, 2, 9 ,8, 6, 7, 5, 2, 3, 1, 2, 0]
k = 36

val = 0
min_val = 30000


for i in range(0, len(list_1)):
    if abs(k-list_1[i]) < min_val:
        val = list_1[i]
        min_val = abs(k-list_1[i])

print(val)
