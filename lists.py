# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(raw_input())
L=[]
append='append'
for i in range(0,N):
    line=raw_input().split()
    command=line[0]
    if command==append:
    	L.append(int(line[1]))
    if command=="insert":
    	L.insert(int(line[1]),int(line[2]))
    if(command=="remove"):
    	L.remove(int(line[1]))
    if(command=="pop"):
    	L.pop()
    if(command=="sort"):
    	L.sort()
    if(command=="reverse"):
    	L.reverse()
    if(command=="print"):
    	print L
