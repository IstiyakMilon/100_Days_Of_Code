def birthdayCakeCandles(ar):
  ar.sort()
  # maxHeightCandles=ar[-1]
  maxCount=ar.count(ar[-1])
  return maxCount

print(birthdayCakeCandles([1, 2, 3, 3, 3]))