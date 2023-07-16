# input = 20, 21, 22; output = 32
klass_1 = int(input('Введите число учеников 1 класса:'))
klass_2 = int(input('Введите число учеников 2 класса:'))
klass_3 = int(input('Введите число учеников 3 класса:'))

desk_1 = klass_1//2 + klass_1 % 2
desk_2 = klass_2//2 + klass_2 % 2
desk_3 = klass_3//2 + klass_3 % 2

sum = desk_3 + desk_2 + desk_1
print(sum)


