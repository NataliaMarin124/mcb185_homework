# 38quiz.py by Natalia Marin and Roger Xu and Yutong Ji 

pi = 3
sign = -1
for n in range(1, 30, 2):
	pi = 4 *(1 + sign*(1/(n+2)))
	print(n, sign, pi)
	

	sign = -sign  
	