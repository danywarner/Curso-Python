n=raw_input()
L=list(map(int,raw_input().split(' ')))
L.sort()
largest= L[-1]
while(L[-1]==largest):
	L.pop()
print L[-1]
