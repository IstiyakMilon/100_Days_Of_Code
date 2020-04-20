def sockMerchant(n, ar):
  sockFreq={}
  sockPair=0
  for item in ar:
    if item in sockFreq:
      sockFreq[item]+=1
    else:
      sockFreq[item]=1
  for key, value in sockFreq.items():
    sockPair+=value//2
  return sockPair

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))