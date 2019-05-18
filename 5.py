def minmax(a): 
	for i in a:
		
		minpos = a.index(min(a)) 		
		maxpos = a.index(max(a))
	
		if maxpos < minpos:
			a.pop(a.index(max(a)))

a = ['h', 'z', 'a', 'c', 'd', 'b']
minmax(a)
print([min(a), max(a)])
