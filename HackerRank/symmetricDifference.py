n=int(input())
x=list(map(int, input().strip().split()))
setA=set(x)
n1=int(input())
y=list(map(int, input().strip().split()))
setB=set(y)
A=setA.difference(setB)
B=setB.difference(setA)
r=A.union(B)
for item in sorted(r):
    print(item)