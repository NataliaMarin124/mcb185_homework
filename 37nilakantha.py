# 37nilakantha.py by Natalia Marin 


pi = 3
sign = 1
for n in range(2, 15, 2):
	pi = pi + sign*(4/ (n * (n +1) * (n+2)))
	print(n, n+1, n+2, sign, pi)
	

	sign = -sign  


