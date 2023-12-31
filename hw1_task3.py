#Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
#и получали билет с номером.
#Счастливым билетом называют такой билет с шестизначным номером, 
#где сумма первых трех цифр равна сумме последних трех.
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
#Вам требуется написать программу, которая проверяет счастливость
#билета с номером n и выводит на экран yes или no.

#Пример:
#n = 385916 -> yes
#n = 123456 -> no
n = 125143

s1 = n // 1000 # первые три цифры числа
s2 = n % 1000 # последние три цифры числа
sum1 = s1 // 100 + (s1 // 10) % 10 + s1 % 10 # нахождение каждой цифры и сумма
sum2 = s2 // 100 + (s2 // 10) % 10 + s2 % 10 

if sum1 == sum2:
    print('yes')
else:
    print('no')
