# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split())
# print(n)
marks_Arr=[]
for _ in range(x):
    arr=list(map(float, input().strip().split()))
    marks_Arr.append(arr)

for x in zip(*marks_Arr):
  print(sum(x)/len(x))