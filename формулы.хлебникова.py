import math
x = float(input())
y = float(input())
z = float(input())
s = 2 ** (y ** x) + (3 ** x) ** y - (y * (math.atan(-1/3)))/(abs(x) + 1/(y**2 + 1))
print(s)
