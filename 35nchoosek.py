# 35nchoosek.py by Natalia Marin 

def factorial(x):
	if x == 0: 
		return 1
	fac = 1
	for i in range(1, x + 1):
		fac = fac * i 
	return fac

def nchoosek(n, k):
	if n < k: 
		return 0
	return factorial(n) / (factorial(k) * factorial(n - k))
	
print(nchoosek(6, 2))