#74genefinder.py by Natalia Marin 
#program reports putative coding genes 

import mcb185
import sys

fasta = sys.argv[1]
min_len = int(sys.argv[2])

def cds_finder(seq):
	coordinates  = {}
	stop_codon   = ['TAA', 'TAG', 'TGA']
	start_codon = 'ATG'
	#create a loop for the reading frames 0, 1, 2
	for frame in range(3):
		i = frame
		while i < len(seq):
			codon = seq[i:i+3]
			if codon == start_codon:
				start_index = i 
				for j in range(i+3, len(seq), 3):
					codon = seq[j:j+3] 
					if codon in stop_codon: 
						stop_index = j
						if stop_index - start_index >= min_len:
							coordinates[start_index] = stop_index + 2
						break			
			i += 3
	return coordinates 

for defline, seq in mcb185.read_fasta(fasta):
	name = defline.split()
	name_sec = defline[0:29]
	#print(name_sec)
	rev_seq = mcb185.anti_seq(seq)
	coordin_negative = cds_finder(rev_seq)
	coordin_positive = cds_finder(seq)
	for k, v in coordin_positive.items():
		print(name_sec,'  RefSeq', '  CDS', '  ', k, '  ', v, '  .  ', '+', '  ID=cds')
	for k, v in coordin_negative.items():
		km = len(seq) - k - 1
		vm = len(seq) - v - 1
		print(name_sec,'  RefSeq', '  CDS', '  ', vm, '  ', km, '  .  ', '-', '  ID=cds' )






"""	
		#seq at starting at different frames relative to the range
		frame_seq   = seq[frame:]
		#print(frame_seq)

		#loop will go length of frame_seq
		#create codon window here
		for i in range(0, len(frame_seq)-3 +1, 3):
			codon = frame_seq[i:i+3]
			#print(i, codon)
		
			#find position of start codon
			if codon == 'ATG': 
				start_index = frame_seq.index(codon)
				print('start frame =', frame, start_index)


			#find position of stop codon
			if codon == 'TGA' or codon == 'TAG' or codon == 'TAA':
				stop_index = frame_seq.index(codon)
				#print('stop frame =', frame, stop_index)

			#checking for length criteria
			if stop_index - start_index >= nt_length:
				#print(start_index, stop_index)
"""


