def solution(items, index, default_value):
  if index<0:
    if abs(index)>len(items):
      return default_value
    else:
      return items[index]
  elif index>=0:
    if index>(len(items)-1):
      return default_value
    else:
      return items[index]

print(solution([1,2,3,4], 3, 'a'))