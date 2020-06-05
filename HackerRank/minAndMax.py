import numpy
Narr=list(map(int, input().split()))
inputArr=[]
for _ in range(Narr[0]):
    ar=list(map(int, input().split()))
    inputArr.append(ar)

minAxis1=numpy.min(inputArr, axis = 1)
print(max(minAxis1))