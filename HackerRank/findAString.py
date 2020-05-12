def count_substring(string, sub_string):
  strLen=len(string)
  subStrLen=len(sub_string)
  countStr=0
  # newSub=[]
  for i in range(strLen-subStrLen+1):
    # newSub.append(string[i:i+subStrLen])
    if string[i:i+subStrLen]==sub_string:
      countStr+=1
  return countStr


print(count_substring("ABCDCDC", "CDC"))