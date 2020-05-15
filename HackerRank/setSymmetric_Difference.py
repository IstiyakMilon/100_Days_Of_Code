# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
setA=set(map(int, input().split()))
n1=int(input())
setB=set(map(int, input().split()))
A=setA.symmetric_difference(setB)
print(len(A))