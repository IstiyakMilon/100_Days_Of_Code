# Enter your code here. Read input from STDIN. Print output to STDOUT
def exceptions_handling(arr):
  outputList=[]
  for x in arr:
    if x[0].isdigit() and x[1].isdigit():
      try:
        outputList.append(int(x[0])//int(x[1]))
      except:
        outputList.append("Error Code: integer division or modulo by zero")
    elif x[0].isdigit() and not x[1].isdigit():
      outputList.append("Error Code: invalid literal for int() with base 10: '%s'"%(x[1]))
  return outputList
        # try:
        #     outputList.append(int(a)//int(b))
        # except ZeroDivisionError:
        #     outputList.append("Error Code: integer division or modulo by zero")
    # elif a.isdigit() and not b.isdigit():
    #     try:
    #         outputList(int(a)//b)
    #     except ValueError:
    #         outputList.append("Error Code: invalid literal for int() with base 10: '{}'" % (b))
    # # elif not a.isdigit() and

# for x in outputList:
#     print(x)
print(exceptions_handling([['1','1'],['1','0'],['1', '#']]))
errors=exceptions_handling([['1', '0'],['2', '$'],['3', '1']])
for x in errors:
  print(x)