#6
n = int(input())
if n < 0:
    print('факториал отрицательного числа не существует')
else:
    c = 1
    while n > 1:
        c *= n
        n -= 1
    print(c)
        
