# 57birthday.py by Natalia and helped by Roger and Adele

import random
import sys 

trials = int(sys.argv[1])
days   = int(sys.argv[2])
people = int(sys.argv[3])

duplicates = 0
for i in range(trials): 
	calendar = []
	for i in range(days)
		calendar.append(0)
	for j in range(people)
		birthday = random.randint(1, days - 1)
		calendar[birthday] +=1
		if calendar[birthday] > 1:
			duplicate += 1
			break 
		
print(duplicates / trials)