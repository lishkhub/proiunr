def pr(n):
    for i in str(n):
        i = int(i)
        if i == 0 or n % i != 0:
            return 0
    return 1

n = int(input('введите n - '))
o = []
for i in range(1, n + 1):
    if pr(i):
        o.append(i)
print(o)
