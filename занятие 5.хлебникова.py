import random
k = int(input('конец промежутка '))
m = []
s = 1
while s != 0:
    s = random.randint(0, k)
    m.append(s)

povt = {}
for x in m:
    if x in povt:
        povt[x] += 1
    else:
        povt[x] = 1
mx = max(povt.values())
print(mx)

