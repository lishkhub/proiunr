def prost(n, d = 2):
    if d ** 2 > n:
        return True
    if n % d == 0:
        return False
    return prost(n, d + 1)

n = int(input('введите n:'))
if n <= 1:
    print('введите число больше 1')
else:
    if prost(n):
        print('YES')
    else:
        print('NO')
