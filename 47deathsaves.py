# 47deathsaves.py by Natalia Marin 

import random 

def death_saves():
	success = 0
	failure = 0
	status = True
	
	while status:
		r1 = random.randint(1, 20)
	
		if r1 >= 10:
			if r1 == 20:
				status   = False
				statusup = 'revived'
			else:       success += 1
		else:
			if r1 == 1: failure += 2
			else:       failure += 1
		if success >= 3:
			status   = False
			statusup = 'stable'
		if failure >= 3: 
			status   = False
			statusup = 'dead' 
	return statusup
	
rc = 0
sc = 0
dc = 0

for i in range(1, 5001):
	roll = death_saves()
	if roll == 'revived': rc += 1
	if roll == 'stable' : sc += 1
	if roll == 'dead'   : dc += 1
print(f'P(revived)= {rc / 5000}, P(stable) = {sc / 5000}, P(death) = {dc / 5000}')
	
			