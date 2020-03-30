def disemvowel(string):
  outputString=""
  for char in string:
    if char=="e":
      continue
    elif char=="E":
      continue
    elif char=="A":
      continue
    elif char=="a":
      continue
    elif char=="i":
      continue
    elif char=="I":
      continue
    elif char=="o":
      continue
    elif char=="O":
      continue
    elif char=="u":
      continue
    elif char=="U":
      continue
    outputString +=char  
  return outputString

print(disemvowel("This website Is for losErs LOL!"))