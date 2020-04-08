#Push an item in a stack
def stackPush(arr, item):
  arr.append(item)
  return arr


# Pop an item from a stack
def stackPop(arr):
  top=len(arr)
  if top==0:
    return "The stack is empty"
  else:
    item1=arr.pop()
    return item1
#Reading stack Top value
def stackPeek(arr):
  top=len(arr)
  if top==0:
    return "The Stack is empty"
  return arr[-1]

listInput=[1,2,3,4,5]
print(stackPop(listInput))
print(stackPop(listInput))
print(stackPop(listInput))
print(stackPop(listInput))
print(stackPop(listInput))
print(stackPeek(listInput))
