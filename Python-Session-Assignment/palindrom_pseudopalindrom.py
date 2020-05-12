word="Paka"
Lword=word.lower()
if Lword==Lword[::-1]:
  print("{} is palindrom".format(word))
else:
  print("{} is not palindrom".format(word))

print(Lword[len(Lword):0:-1])
if Lword[1:]==Lword[len(Lword):0:-1]:
  print("{} is pseudo-palindrome".format(word))
else:
  print("{} is not pseudo-palindrome".format(word))