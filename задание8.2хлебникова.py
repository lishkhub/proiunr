m = int(input('длина массива - '))
a = []
for i in range(m):
    e = int(input('элемент массива - '))
    a.append(e)
print(a)
a[0], a[-1] = a[-1], a[0]
print(a)
