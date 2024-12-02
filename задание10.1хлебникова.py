with open('HAA_Y-244_vvod.txt', 'w') as matr:
    n = int(input("порядок матрицы "))
    for i in range(n):
        e = input('введите элементы через пробел:')
        matr.write(e + '\n')

with open('HAA_Y-244_vvod.txt', 'r') as matr:
    s = matr.readlines()
    m = [list(map(int, line.split())) for line in s]

with open('HAA_Y-244_vivod.txt', 'w') as o:
    for i in range(len(m[0])):
        n = []
        for t in range(len(m)):
            n.append(m[t][i])
        o.write(''.join(map(str, n)) + '\n')
print("новая матрица:")
for e in range(len(m[0])):
    print(' '.join(map(str, [m[t][e] for t in range(len(m))])))



