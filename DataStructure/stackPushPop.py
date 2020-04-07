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

def stackPeek(arr):
  return arr[-1]

listInput=[1,2,3,4,5]
print(stackPush(listInput, 11))
print(stackPop(listInput))
print(stackPop(listInput))
print(stackPop(listInput))
print(stackPeek(listInput))
