#Разложение числа на простые множители

while True:
    n = int(input('Введите число:'))
    if n >= 1:
        break

res = []
temp = 2

while n > 1:
    if n % temp == 0:
        res.append(temp)
        n //= temp
    else:
        temp += 1
print(res)