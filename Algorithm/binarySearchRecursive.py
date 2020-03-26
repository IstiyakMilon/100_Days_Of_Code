
def binarySearch(list, l, r, item):
  if r>=l:
    mid=int(l+(r-l)/2)
    if list[mid]==item:
      return mid
    elif list[mid]>item:
      return binarySearch(list,l, mid-1, item)
    else:
      return binarySearch(list, mid+1, r, item)
  
  return -1


arr=[2, 3, 4, 5, 6, 8, 10, 11, 12]
x=11
n=len(arr)
# print(type(n))
result=binarySearch(arr, 0, n-1, x)
# print(result)
if result>-1:
  print("The item is found at index %d" %(result))
else:
  print("The item is not found")