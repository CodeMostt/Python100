#l=[4,343,242,13,52,5]
def ssort(l):
	for start in range(len(l)):
		minpos=start
		for i in range(start,len(l)):
			if(l[i]<l[minpos]):
				minpos=i
		(l[start],l[minpos])=(l[minpos],l[start])
	return l
print(ssort([2,3,1,5,6]))
