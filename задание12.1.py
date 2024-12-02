import sys

def st(x, n):
    if n == 0:
        return 1
    return x * st(x, n - 1)

def fl(n):
    if n == 0:
        return 1
    return n * fl(n - 1)

sys.setrecursionlimit(10000)
x = int(input('введите x:'))
n = int(input('введите n:'))
if n < 0:
    print('n должно быть натуральным')
else:
    print(st(x, n)/fl(n))
