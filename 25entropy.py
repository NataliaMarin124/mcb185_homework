# 25entropy.py 
import math 

def shannon_entropy(a, c, g, t):
	h=0								#starting entropy value 					
	total_nuc = a + g + c + t
	
	a_prob = a/total_nuc
	c_prob = c/total_nuc
	g_prob = g/total_nuc
	t_prob = t/total_nuc 
	
	
	if a_prob != 0: h = h + (a_prob * math.log(a_prob, 2))
	if c_prob != 0: h = h + (c_prob * math.log(c_prob, 2))
	if g_prob != 0: h = h + (g_prob * math.log(g_prob, 2))
	if t_prob != 0: h = h + (t_prob * math.log(t_prob, 2))
	return -h

#sample runs
print(shannon_entropy(12, 5, 9, 12))
print(shannon_entropy(0, 19, 11, 2))
print(shannon_entropy(0, 0, 23, 31))