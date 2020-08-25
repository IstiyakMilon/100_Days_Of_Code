# Enter your code here. Read input from STDIN. Print output to STDOUT
# list1=list(map(int, input().split(" ")))
# list2=list(map(int, input().split(" ")))
# outputList=[(x,y) for x in list1 for y in list2]
# print(*outputList)
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))
list1=list(product(a,b))
print(*list1)