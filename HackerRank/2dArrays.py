def twoDArrays(arr):
  iLength=len(arr)
  jLength=len(arr[0])
  sumArr=[]
  for i in range(iLength-2):
    for j in range(jLength-2):
      hourSum=arr[i][j]+arr[i][j+1]+arr[i][j+2]
              +arr[i+1][j+1]+arr[i+2][j]
              +arr[i+2][j+1]+arr[i+2][j+2]
      sumArr.append(hourSum)
  return(max(sumArr))


print(twoDArrays([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0
]]))