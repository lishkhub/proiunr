import random 
m = []
n = 25
s = 0
for i in range(n):
	m.append(random.randint(0,50))
	s += m[i]
for i in range(n):
    if i % 10 == 0:
        m[i] = s/n

print(m)
