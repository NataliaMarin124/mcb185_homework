#test_dogma.py by Natalia Marin 

import dogma

print(dogma.transcribe('ACGTAUGGATTAG'))
print(dogma.reversecomp('AAAACGT'))
print(dogma.translate('ATGGATTTACCTCTCAUGTAA')) #should return M*

s = 'ACGTGGGGGGCATATG'
print(dogma.gc_comp(s))
print(dogma.gc_skew(s), dogma.reversecomp(s))