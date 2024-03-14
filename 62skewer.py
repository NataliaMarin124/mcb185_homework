#62skewer.py by Natalia Marin + coderie sessions
#more efficient version of 61skewer.py

import sys
import mcb185

genome = sys.argv[1]
w      = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(genome):
#get gc counts for first window
	init = seq[:w]
	g = init.count('G')
	c = init.count('C')
#get gc count for all other windows
for i in range(len(seq) - w):
	off = seq[i]
	if   off == 'G': g -= 1
	elif off == 'C': c -= 1
	
	on  = seq[i+w]
	if   on == 'G': g += 1
	elif on == 'C': c += 1
	
	if g+c == 0: continue
	print(i, off, on, (g+c)/w, (g-c)/(g+c))
	




