# def multipleOf3and5(n):
#   list=[]
#   for i in range(1, n):
#     if i%3==0 and i%5==0:
#       list.append(i)
#     elif i%3==0:
#       list.append(i)
#     elif i%5==0:
#       list.append(i)
#   return sum(list)
def solution(number):
  list=[]
  for i in range(1, number):
    if i%3==0 and i%5==0:
      list.append(i)
    elif i%3==0:
      list.append(i)
    elif i%5==0:
      list.append(i)
  return sum(list)


print(solution(10))