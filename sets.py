M=raw_input()
arr=set(map(int,raw_input().split(' ')))
M=raw_input()
arr2=set(map(int,raw_input().split(' ')))
arr3=arr.difference(arr2)
arr4=arr2.difference(arr)
arr5=arr3.union(arr4)
L=list(arr5)
L.sort()
for i in range(0,len(L)):
	print L[i]
