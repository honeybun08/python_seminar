#Дано натуральное число A > 1. Определите, каким по
#счету числом Фибоначчи оно является, то есть
#выведите такое число n, что φ(n)=A. Если А не
#является числом Фибоначчи, выведите число -1.
#Input: 5
#Output: 6 

n = int(input('Введите число -> '))
if(n == 0):
    print(1)
else:
    first,second,count = 0,1,2 #
    while second <= n:
        if(second == n):
            print(count)
            break
        first, second = second, first + second
        count += 1
    else:
        print(-1)