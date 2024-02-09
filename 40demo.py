# 40demo.py by Natalia Marin 

import random 

for i in range(5):
	for j in range(1):
		print(random.random())
	
for i in range(5):
	print(random.choice('ACGT'), end=' ')
print()

for i in range(50):
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end=' ')
	else:       print(random.choice('CG'), end=' ')
print()


for i in range(3):
	print(random.randint(1, 6))
	
for i in range(7):
	print(random.gauss(0, 1.0))

print('this line\n has some\n line breaks')

print('a\tb\tcat\tdogma')

print(10, 20, 30, 40, sep='\t')

i = 1
pi = 3.14149
print('normal string {i} {pi}')
print(f'formatted string {i} {pi:.3f}')
print(f'tau {pi + pi}')

import sys

print('logging', file=sys.stderr)

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())

"""


nts = 'ACGT'

for nt in nts:
	print(nt, end='')
print()

import random 
for i in range(3):
	print('>seq', {i+1}, sep='')
	print(f' >seq-{i+1}')
	for j in range(random.randint(20, 50)):
		print(random.choice(nts), end='')
print()

for nt1 in nts:
	for nt2 in nts:
		if nt2 > nt1:
			print('outer', nt1, 'inner', nt2)
		
limit = 4	
for i in range(limit): 
	for j in range(i+1, limit):
		print(i, j)

#Scoring Matrix hw assignment 

limit = 4	
for i in range(0, limit): 
	for j in range(0, limit):
		if i == j: print('+', end=' ')
		else:      print('-', end=' ')
	print()

"""














