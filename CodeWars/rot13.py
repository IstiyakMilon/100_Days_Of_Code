def rot13(message):
  resultMess=""
  for s in message:
    asci=ord(s)
    if asci>=65 and asci<=77:
      asci+=13
      char=chr(asci)
      resultMess+=char
    elif asci>=78 and asci<=90:
      asci-=13
      char=chr(asci)
      resultMess+=char
    elif asci>=97 and asci<=109:
      asci+=13
      char=chr(asci)
      resultMess+=char
    elif asci>=110 and asci<=122:
      asci-=13
      char=chr(asci)
      resultMess+=char
    else:
      resultMess+=s
  return resultMess


print(rot13("Test"))