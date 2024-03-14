#63dust.py by Natalia Marin + coderie help 

import sys
import mcb185
import math

def shannon_entropy(subseq):
	h      = 0		
	total_nuc = (A + G + T + C)
	a_prob    = A/total_nuc
	c_prob    = C/total_nuc
	g_prob    = G/total_nuc
	t_prob    = T/total_nuc 
	
	if a_prob != 0: h += (a_prob * math.log(a_prob, 2))
	if c_prob != 0: h += (c_prob * math.log(c_prob, 2))
	if g_prob != 0: h += (g_prob * math.log(g_prob, 2))
	if t_prob != 0: h += (t_prob * math.log(t_prob, 2))
	return -h


fasta_file        = sys.argv[1]
window            = int(sys.argv[2])
entropy_threshold = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(fasta_file):
	print(f'>{defline}')
	listseq = list(seq)
	for i in range(len(seq) - window +1):
		subseq  = seq[i:i+window]
		G       = subseq.count('G')
		T       = subseq.count('T')
		A       = subseq.count('A')
		C       = subseq.count('C')
		entropy = shannon_entropy(subseq)
		if entropy < entropy_threshold:
			for j in range(i, i + window):
				listseq[j]= 'N'

	complete_seq = ''.join(listseq)
	print(complete_seq)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		