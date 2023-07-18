#15. Иван Васильевич пришел на рынок и решил
#купить два арбуза: один для себя, а другой для тещи.
#Понятно, что для себя нужно выбрать арбуз
#потяжелей, а для тещи полегче. Но вот незадача:
#арбузов слишком много и он не знает как же выбрать
#самый легкий и самый тяжелый арбуз? Помогите ему!
#Пользователь вводит одно число N – количество
#арбузов. Вторая строка содержит N чисел,
#записанных на новой строчке каждое. Здесь каждое
#число – это масса соответствующего арбуза
#Input: 5 -> 5 1 6 5 9
#Output: 1 9

import random
n = int(input('Введите число арбузов -> '))

watermelons = []
while n > 0:
    watermelons.append(random.randint(1,16))
    n -= 1

print(watermelons)

max_weight = max(watermelons)
min_weight = min(watermelons)
print(f'Ваш арбуз весит {max_weight} кг,'
      f' a aрбуз для тещи весит {min_weight} кг')

max_weight = watermelons[0]
min_weight = watermelons[1]

# защита от дурака
#if min_weight > max_weight:
    #temp = min_weight
    #min_weight = max_weight
    #max_weight = temp

#for i in range(0,len(watermelons)-1):
    #if watermelons[i] > max_weight:
        #max_weight = watermelons[i]
    #if watermelons[i] < min_weight:
        #min_weight = watermelons[i]


#print(f'Ваш арбуз весит {max_weight} кг,'
      #f' a aрбуз для тещи весит {min_weight} кг')

#Ввод ручками
while True:
    n = int(input('Введите кол-во арбузов  -> '))
    if n > 1:
        break

max_weight = 0
min_weight = 30000


while n > 0:
    temp = int(input(f'Введите вес арбуза {n} -> '))
    if min_weight > temp:
        min_weight = temp
    if max_weight < temp:
        max_weight = temp
    n -= 1


print(f'Ваш арбуз весит {max_weight} кг,'
      f' a aрбуз для тещи весит {min_weight} кг')

