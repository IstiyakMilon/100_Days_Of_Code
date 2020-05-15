n = int(input())
s = set(map(int, input().split()))
arr=[]
for _ in range(int(input())):
        command = input().strip().split()
        arr.append(command)
    
for ar in arr:
    if ar[0]=="remove":
      s.remove(int(ar[1]))
    elif ar[0]=="discard":
      s.discard(int(ar[1]))
    elif ar[0]=="pop":
      s.pop()


print(sum(s))