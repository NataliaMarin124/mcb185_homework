# 22oligotemp.py by Natalia_Marin

import math

def melt_oligos(A, T, G, C):
	length = A + T + G + C
	if length <= 13:
		x = (A+T)*2 + (G+C)*4
		return x
		
	if length > 13: 
		x = 64.9 + 41*((G+C - 16.4)/(length))
		return x

#sample runs 
print(melt_oligos(2, 3, 4, 2))
print(melt_oligos(5, 5, 5, 5))
print(melt_oligos(10, 40, 40, 10))
	