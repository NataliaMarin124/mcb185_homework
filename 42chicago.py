#42chicago.py by Natalia Marin 
#program finds average score of Chicago and how often a game ends w/zero
import random 

import sys

"""
#github solution to problem
gamesplayed = 1000
for i in range(gamesplayed):
	score = 0           
#you have to set score=0 inside the loop or game will reset
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target
		print(score) 
"""

gamesplayed = 100000
log = gamesplayed // 100 # report progress at 1% intervals 
zerogames = 0
totalscore = 0
for i in range(gamesplayed):
	if i % log == 0: print(f'{100 * i/gamesplayed:.0f}', file=sys.stderr)
	score = 0
	for round in range(2, 13):        #chicago has 12 rounds total
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == round:
			score += round
	
	totalscore += score	
	if score == 0:
		zerogames+=1
		
print(zerogames / gamesplayed)        #end game with score of zero
print(totalscore/ gamesplayed)        #average score for chicago


