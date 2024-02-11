# 46savingthrows.py by Natalia Marin & class 

import random 

def roll_normal():
	r1 = random.randint(1, 20)
	return r1
	
	
def roll_advantage():
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 > r2:
		return r1
	else:
		return r2

def roll_disadvantage():
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 < r2:
		return r1
	else: 
		return r2
		
		
trials = 1000
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		d = roll_disadvantage()
		if d >= dc:
			success += 1
	print(success / trials)

for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		a = roll_advantage()
		if a >= dc:
			success += 1
	print(success / trials)
	
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		nr = roll_normal()
		if nr > dc:
			success += 1
	print(success / trials)

