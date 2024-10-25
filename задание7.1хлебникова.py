import random 
m = []
n = 25
s = 0
p = 1
for i in range(n):
	m.append(random.randint(1,50))
	s += m[i]
	p *= m[i]
print(m)
print('сумма всех элементов:', s)
print('произведение всех элементов:', p)
