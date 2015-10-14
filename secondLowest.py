def secondLargest(L):
	L.sort()
	L.reverse()
	largest= L[-1]
	while(L[-1]==largest):
		L.pop()
	return L[-1]

n=int(raw_input())
L=[]
L2=[]
L3=[]
for i in range(0,n):
	L.append([raw_input(),float(raw_input())])
L.sort()
for j in L:
	x=0
	L2.append(j[1])
	x+=1
second=secondLargest(L2)
for k in L:
	if k[1]==second:
		L3.append(k[0])
for l in L3:
	print l



