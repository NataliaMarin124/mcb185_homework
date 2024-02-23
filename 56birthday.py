# 56birthday.py by   Natalia Marin helped by Roger and Adele

import sys
import random 

trials = int(sys.argv[1])
days   = int(sys.argv[2])
people = int(sys.argv[3])

duplicates = 0
for i in range(trials): 
	b_days =[]
	for j in range(people):
		birth_d= random.randint(1, days)
		if birth_d in b_days:
			duplicates +=1
			break
		else: 
			b_days.append(birth_d)

print(duplicates/ trials)
	