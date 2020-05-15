# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
x=list(map(int, input().strip().split()))
setA=set(x)
n1=int(input())
y=list(map(int, input().strip().split()))
setB=set(y)
print(len(setA.intersection(setB)))