#64profinder.py by Natalia Marin + coderie help

import dogma
import mcb185
import sys

path = sys.argv[1] 
min_length = int(sys.argv[2]) 

seq_list = []

def profinder(aa, min_length):
	start_index = 0
	stop_index = 0
	new_string = aa
	for i in range(len(aa)):
		# escaping loop when we reach the end 
		# we know when we're done when we know there
		# are no more start codons after the last stop_index
		if aa[stop_index:].find('M') == -1:
			break
		# for first loop
		if i == 0:
			start_index = aa.find('M')
			stop_index = aa.find('*')
		# for anything after 1st loop
		if i != 0: 
			# code below happens if i is not equal to 0
			new_string = aa[stop_index+1:] 
			start_index = stop_index + 1 + new_string.find('M') 
			stop_index = stop_index + 1 + new_string.find('*') 
		if stop_index-start_index >= min_length:
			seq_list.append(aa[start_index:stop_index+1])


for defline, seq in mcb185.read_fasta(path):
	rev_comp = dogma.reversecomp(seq)

	#frames 1, 2, 3, -1, -2, -3
	for i in range(3):
		new_seq = dogma.translate(seq[i:])
		profinder(new_seq, min_length)
		new_seq = dogma.translate(rev_comp[i:])
		profinder(new_seq, min_length)
	
	# all sequences stored in seq_list
	# print in FASTA format 
	name = defline.split()  
	the_name = name[0]
	for i in range(len(seq_list)):
		print(f'>{the_name}-prot-{i}')
		print(seq_list[i])


























	