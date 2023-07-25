# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Пример:
# k = 'ноутбук'
# 12



# dict_eng = {
#         1: "А, В, Е, И, Н, О, Р, С, Т",
#         2: "Д, К, Л, М, П, У",
#         3: "Б, Г, Ё, Ь, Я",
#         4: "Й, Ы",
#         5: "Ж, З, Х, Ц, Ч",
#         8: "Ш, Э, Ю",
#         10: "Ф, Щ, Ъ"
#     }

# dict_rus = {
#         1: "A, E, I, O, U, L, N, S, T, R",
#         2: "D, G",
#         3: "B, C, M, P",
#         4: "F, H, V, W, Y",
#         5: "K",
#         8: "J, X",
#         10: "Q, Z"
#     }

# k = input('Введите слово:').upper()
# word_list = list()

# for letter in k:
#     word_list.append(letter)

# # print(word_list)
# points = 0

# for i in word_list:
#     for key in dict_rus:
#         for j in dict_rus[key]:
#             if j == i: # если j по ключу равен i по букве, то прибавляем стоимость в points
#                 points += key

# for i in word_list:
#     for key in dict_eng:
#         for j in dict_eng[key]:
#             if j == i:
#                 points += key

# print(points)



# import re
# def Scrabble(text):
# 	return bool(re.search("[а-яА-Я]", text))
# Rus = { 1:"А, В, Е, И, Н, О, Р, С, Т",
#       	2:"Д, К, Л, М, П, У",
#         3:"Б, Г, Ё, Ь, Я",
#         4:"Й, Ы",
#         5:"Ж, З, Х, Ц, Ч",
#         8:"Ш, Э, Ю",
#         10:"Ф, Щ, Ъ"}
# Eng = { 1:"A, E, I, O, U, L, N, S, T, R ",
#         2:"D, G",
#         3:"B, C, M, P",
#         4:"F, H, V, W, Y",
#         5:"K",
#         8:"J, X"}
# text = input("Введите слово: ").upper()
# if Scrabble(text):
# 	print(sum([k for i in text for k, v in Rus.items() if i in v]))
# else:
# 	print(sum([k for i in text for k, v in Eng.items() if i in v]))

k = 'ноутбук'

dict = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}

k = k.upper()

points = 0

for i in k:
    for k, v in dict.items():
        if i in v:
            points += k
            
print(points)
