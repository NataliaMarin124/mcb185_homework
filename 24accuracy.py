# 24accuracy.py by Natalia_Marin

def performance(tp, fp, tn, fn):
	p = tp/(tp+fp)				#defining formulas for precision(p), recall (r)
	r = tp/(tp+fn)
	f1_score = 2*((p*r)/(p+r))
	accuracy = (tp+tn)/ (tp+tn+fp+fn)
	return f1_score and accuracy 
	
#sample runs 
print(performance(2, 4, 8, 1))
print(performance(99, 3, 130, 6))
print(performance(100, 200, 500, 47))