def migratoryBirds(arr):
  listDict={}
  for item in arr:
    if item in listDict:
      listDict[item]+=1
    else:
      listDict[item]=1
  # print(listDict)
  listTuple=[]
  for item, value in listDict.items():
    listTuple.append((value, item))
  sortedTuple=sorted(listTuple)
  # print(sortedTuple)
  max=0
  for i in range(len(sortedTuple)-1):
    if sortedTuple[i][0]<sortedTuple[i+1][0]:
      max=i+1
  print(sortedTuple[max][1])

migratoryBirds([1, 4, 4, 4, 5, 3])