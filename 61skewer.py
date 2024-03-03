#61skewer.py by Natalia Marin 

import dogma

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10 # looks at 10 nts at a time
for i in range(len(seq) -w +1): #moves the len of seq by one nt
	s = seq[i:i+w] # this creates the seq as window shifts?
#	print(i, dogma.gc_comp(s), dogma.gc_skew(s))
	print(f'{i}\t{dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')