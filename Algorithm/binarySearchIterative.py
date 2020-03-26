def binarySearch(arr, l, r, item):
  while l<=r:
    mid=int(l+(r-l)/2)
    if arr[mid]==item:
      return mid
    elif arr[mid]<item:
      l=mid+1
    elif arr[mid]>item:
      r=mid-1
  return -1


list=[1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
n=len(list)
x=int(input("Enter the number: "))
result=binarySearch(list, 0, n-1, x)
if result>-1:
  print("The item is found at index %d" %(result))
else:
  print("The item is not found in the list")
