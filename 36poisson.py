# 36poisson.py  by Natalia Marin 

import math 

def factorial(x):
	if x == 0: 
		return 1
	fac = 1
	for i in range(1, x + 1):
		fac = fac * i 
	return fac
	
def poisson(n, k):
	i = (n**k * math.e**(-n)) / factorial(k)
	return i 

print(poisson(4, 3))
print(poisson(6, 2))
print(poisson(14, 13))