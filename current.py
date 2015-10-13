# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(raw_input())

for i in range(0,N):
    name, a, b,c = raw_input().split()
    a,b,c = float(a),float(b),float(c)
    dic[name]=((a+b+c)/3.00)
particular = raw_input()
print("%.2f" % dic[particular])



