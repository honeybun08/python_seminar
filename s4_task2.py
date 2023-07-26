# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

import re
print(len(set(re.split(' |\\.', input('Введите текст -> ').lower()))))
# делаем все в нижний регистр, убераем знаки, превращаем во множесто(все уникальное остается) и выводим длину множества
