def find_missing_letter(chars):
  for i in range(0, len(chars)-1):
     previousCharAscii=ord(chars[i])
     nextCharAscii=ord(chars[i+1])
     diff=nextCharAscii-previousCharAscii
     if diff>1:
       return chr(previousCharAscii+1)
  


print(find_missing_letter(['A','B','D']))