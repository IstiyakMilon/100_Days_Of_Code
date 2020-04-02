def solution(n,d):
  resultList=[]
  if d>0:
    Str=str(n)
    nStr=Str[-d:]
    # print(nStr)
    for char in nStr:
      resultList.append(int(char))
    return resultList
  return resultList
print(solution(101,0))