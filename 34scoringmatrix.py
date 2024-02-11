# 34scoringmatrix.py by Kenta Hsu and Natalia Marin 

nts = 'ACGT'
for nt in nts:
	print(nt, end=' ')

def printmat(nts):
	limit = len(nts)
	for i in range(limit):
		for j in range(limit):
			if i == j: print('+', end='')
	print()
			

"""
def scoringmatrix():
	nts = 'ACGT'
	print(' ', end='')
	for nt in nts:
		print('  ', end='')
		print(nt, end='')
	print()
	for nt in nts:
		print(nt, end=' ')
		for nt2 in nts:
			if nt == nt2:
				print('+1', end=' ')
			else:
				print('-1', end=' ')
		print()





scoringmatrix()
"""

