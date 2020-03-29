def complementaryDNA(inputDNA):
  outputDNA=""
  for char in inputDNA:
    if char=="A":
      outputDNA+="T"
    elif char=="T":
      outputDNA+="A"
    elif char=="G":
      outputDNA+="C"
    elif char=="C":
      outputDNA+="G"
      
  return outputDNA
print(complementaryDNA("ATGC"))