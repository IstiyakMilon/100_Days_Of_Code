def correct_polish_letters(st): 
  resultStr=""
  for char in st:
    if char=='ą':
      resultStr+='a'
    elif char=='ć':
      resultStr+='c'
    elif char=='ę':
      resultStr+='e'
    elif char=='ł':
      resultStr+='f'
    elif char=='ń':
      resultStr+='f'
    elif char=='ó':
      resultStr+='o'
    elif char=='ś':
      resultStr+='s'
    elif char=='ź':
      resultStr+='z'
    elif char=='ż':
      resultStr+='z'
    else:
      resultStr+=char
  return resultStr

print(correct_polish_letters('Jedrzej Bfadzifski'))
print(correct_polish_letters('Lech Wafesa'))
print(correct_polish_letters('Maria Skfodowska-Curie'))
print(correct_polish_letters('Jędrzej Błądziński'))
print(correct_polish_letters('k,ioazzpefpcjo'))