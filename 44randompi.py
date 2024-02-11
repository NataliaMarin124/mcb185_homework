#44randompi.py by Natalia Marin 
#program estimates pi using Monte Carlo methods 

import random

def montecarlo_pi():
	incircle	= 0
	outcircle 	= 0
	totalvalues = 0
	
	while True:
		x = random.random()
		y = random.random()
		distance = (x**2 + y**2)**.5
		
		if distance < 1: 
			incircle += 1
		
		totalvalues +=1
		
		pi = (incircle / totalvalues) * 4
		print('Iteration:', totalvalues, 'pi:', pi )

montecarlo_pi()

		
			