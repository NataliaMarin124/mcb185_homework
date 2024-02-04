# 33triples.py by Natalia Marin 

import math 

for a in range(1, 100):
	for b in range(1, 100):
		c = math.sqrt(a**2 + b**2)
		if math.isclose(c // 1, c) == True:
				print( a, b, c)


	