# 45dndstats.py by Natalia Marin & class

import random 

rolls = 100000
total_3d6 = 0
for i in range(rolls):
	score = 0 
	for j in range(3):
		d = random.randint(1, 6)
		score += d
	total_3d6 += score
print(total_3d6 / rolls)


total_3d6r1 = 0
for i in range(rolls):
	score = 0
	for j in range(3):
		d = random.randint(1, 6)
		if d == 1: 
			d = random.randint(1, 6) 
		score += d
	total_3d6r1 += score
print(total_3d6r1 / rolls)
		
	
total_3d6x2 = 0
for i in range(rolls):
	score = 0
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 > d2: 
			score += d1
		else:
			score += d2
	total_3d6x2 += score
print(total_3d6x2 / rolls)

total_4d61 = 0
for i in range(rolls):
	score = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	
	if d1 < d3 and d1 < d4 and d1 < d2: 
		score += d2 + d3 + d4
	elif d2 < d1 and d2 < d3 and d2 < d4 : 
		score += d1 + d3 + d4
	elif d3 < d1 and d3 < d2 and d3 < d4: 
		score += d1 + d2 + d4
	else: 
		score += d1 + d2 + d3
	total_4d61 += score
print(total_4d61/ rolls)
	
