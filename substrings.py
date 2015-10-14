string = raw_input()
string2 = raw_input()
x=0
a=0
n=len(string)-len(string2)+1
b=n
for i in range(0, n):
	if string.find(string2,i,i+len(string2))!=-1:
		x+=1
	a+=1
	b+=1
print x