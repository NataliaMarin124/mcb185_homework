#65transmembrane.py by Natalia Marin + Kenta Hsu

import dogma
import mcb185
import sys


path = sys.argv[1]

# in: entire FASTA aa entires
# out: list containing deflines that has signal peptide
def signal_peptide_check(path):
	sig_pep_list = []
	for defline, seq in mcb185.read_fasta(path):
		w = 8	
		signal_seq = seq[:30] # slicing first30 aa

		for i in range(len(signal_seq)-w +1):
			window_seq = signal_seq[i:i+w] # string of 8 letters
			# next get hydrophobicity value for everything in window_seq
			# create a sum variable
			total = 0
			for aa in window_seq:
				hydro_value = dogma.hyrdo_aminoacid(aa)
				total += hydro_value
			# we got our sum value
			# now we got our average 
			average = total / w
			if average >= 2.5 and 'P' not in window_seq:
				sig_pep_list.append((defline, seq))
				break
	return sig_pep_list

sig_pep_list = signal_peptide_check(path)
# transmembrane check
# in: defline and seqs that passed signal peptide check
# out: deflines that passed transmembrane check
trans_pep_list = []
for defline, seq in sig_pep_list:
	trans_seq = seq[30:]
	w = 11
	for i in range(len(trans_seq)-w +1):
		window_seq = trans_seq[i:i+w] # string of 8 letters
		# next get hydrophobicity value for everything in window_seq
		# create a sum variable
		total = 0
		for aa in window_seq:
			hydro_value = dogma.hyrdo_aminoacid(aa)
			total += hydro_value
		# we got our sum value
		# now we got our average 
		average = total / w
		if average >= 2 and 'P' not in window_seq:
			trans_pep_list.append(defline)
			break
# print
for defline in trans_pep_list:
	print(defline)
