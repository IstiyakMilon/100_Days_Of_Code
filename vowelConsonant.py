def vowelConsonant(s):
  if (s>='a' and s<='z') or (s>='A'and s<='Z'):
    if s in "aeiouAEIOU":
      print("Vowel")
    else:
      print("Consonant")
  else:
    print("Nothing")

vowelConsonant('A')