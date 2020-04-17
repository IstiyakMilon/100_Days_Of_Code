t=int(input())
inputlist=[]
# t=int(t)

for i in range(t):
    inputString=input()
    inputlist.append(inputString)
for s in inputlist:
  evenStr=""
  oddStr=""
  for j in range(len(s)):
    if j%2==0:
      evn=s[j]
      evenStr+=evn
    else:
      odd=s[j]
      oddStr+=odd
  print("%s %s" % (evenStr, oddStr))