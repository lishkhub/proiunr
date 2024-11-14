n = int(input("порядок матрицы "))
matr = []
for i in range(n):
    e = list(map(int, input('введите элементы через пробел:').split()))
    matr.append(e)
nmatr = [[0] * n for _ in range(n)] 
for i in range(n):
    for t in range(n):
        nmatr[t][i] = matr[i][t] 
print("новая матрица:")
for e in nmatr:
    print(' '.join(map(str, e)))
