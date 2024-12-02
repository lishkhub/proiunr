with open('HAA_Y-244_vvod.txt', 'r') as matr:
    n = int(matr.readline().strip())
    matr = [list(map(int, line.split())) for line in matr.readlines()]
k = int(input("введите номер строки: "))
if k < 0 or k >= n:
    print("строка вне матрицы")
else:
    d = matr[k][k]
    if d == 0:
        print("диагональный элемент 0")
    else:
        for t in range(n):
            matr[k][t] /= d
    with open('HAA_Y-244_vivod.txt', 'w') as wr:
        wr.write('Обновленная матрица:')
        for e in matr:
            wr.write(' '.join(map(str, e)) + '\n')
    print("Обновленная матрица:")
    for e in matr:
        print(' '.join(map(str, e)))
