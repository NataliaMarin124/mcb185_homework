# 21quadratic.py by Natalia_Marin

import math 
import sys

def quad_formula(a, b, c,):
	if a == 0: sys.exit('error: a must be greater than 0') 
	
	d = b**2 - 4*a*c
	if d < 0: 
		print('no real solution')
	elif d == 0: 
		x = (-b + math.sqrt(b**2 - 4 *a *c))/(2*a)
		print('one solution')
		return x 
	else:
		x1 = (-b + math.sqrt(b**2 - 4 * a * c))/(2*a)
		x2 = (-b - math.sqrt(b**2 - 4 * a * c))/(2*a)
		print('two solutions')
		return x1, x2
		
#sample runs
print(quad_formula(2, 3, 1))
print(quad_formula(-3, -1, 2))
print(quad_formula(-4, -6, 7))
print(quad_formula(1, 2, 1))
