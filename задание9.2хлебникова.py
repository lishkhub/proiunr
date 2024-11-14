n = int(input("порядок матрицы "))
matr = []
for i in range(n):
    e = list(map(int, input('элементы через пробел ').split()))
    matr.append(e)
k = int(input("введите номер строки "))
if k < 0 or k >= n:
    print("строка вне матрицы")
else:
    d = matr[k][k]
    if d == 0:
        print("диагональный элемент 0")
    else:
        for t in range(n):
            matr[k][t] /= d 
        print("Обновленная матрица:")
        for e in matr:
            print(' '.join(map(str, e)))
