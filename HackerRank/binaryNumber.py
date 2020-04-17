def decimalToBinary(num):
  s=""
  while num>0:
    d=str(num%2)
    s+=d
    num=num//2
  return s[::-1]   


print(decimalToBinary(13))


def binaryNumber(n):
  binaryNumStr=decimalToBinary(n)
  binaryNumStr=binaryNumStr.split("0")
  maxOne=0
  for ss in binaryNumStr:
    numLength=len(ss)
    if numLength>maxOne:
      maxOne=numLength
  return maxOne

print(binaryNumber(5))
