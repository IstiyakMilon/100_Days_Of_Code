def countApplesAndOranges(s, t, a, b, apples, oranges):
  resultApple=0
  resultOrange=0
  for i in apples:
    appleDist = a+i
    if appleDist>=s and appleDist<=t:
      resultApple+=1
  for i in oranges:
    orangeDist=b+i
    if orangeDist>=s and orangeDist<=t:
      resultOrange+=1
  return [resultApple, resultOrange]

print(countApplesAndOranges(7, 11, 5, 15,[-2, 2, 1], [5, -6]))