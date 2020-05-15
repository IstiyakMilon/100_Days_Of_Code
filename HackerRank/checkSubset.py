# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input().strip())):
    n=int(input().strip())
    x=tuple(map(int, input().strip().split()))
    setA=set(x)
    n1=int(input().strip())
    y=tuple(map(int, input().strip().split()))
    setB=set(y)
    print(setA.issubset(setB))