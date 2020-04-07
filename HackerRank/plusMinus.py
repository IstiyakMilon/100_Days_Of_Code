def plusMinus(arr):
  length=len(arr)
  plus=0
  minus=0
  zero=0
  for i in range(length):
    if arr[i]==0:
      zero+=1
    elif arr[i]>0:
      plus+=1
    elif arr[i]<0:
      minus+=1
  positiveProb=plus/length
  negativeProb=minus/length
  zeroProb=zero/length
  print("%.6f" % positiveProb)
  print("%.6f" % negativeProb)
  print("%.6f" % zeroProb)

plusMinus([-4, 3, -9, 0, 4, 1 ])