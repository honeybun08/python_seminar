#Найдите сумму цифр трехзначного числа n.
#Результат сохраните в перменную res.

# Пример:
#n = 123 -> res = 6 (1 + 2 + 3)
#n = 100 -> res = 1 (1 + 0 + 0)

n = 123

first_digit = n % 10
second_digit = (n % 100) // 10
third_digit = n // 100

res = first_digit + second_digit + third_digit
print(res)
