# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
setA=set(map(int, input().split()))


for _ in range(int(input())):
        commandArr = input().strip().split()
        setB=set(map(int, input().split()))
        if commandArr[0]=='intersection_update':
            setA.intersection_update(setB)
        elif commandArr[0]=='update':
            setA.update(setB)
        elif commandArr[0]=='symmetric_difference_update':
            setA.symmetric_difference_update(setB)
        elif commandArr[0]=='difference_update':
            setA.difference_update(setB)
    

print(sum(setA))