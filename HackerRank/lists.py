def lists(arr):
  result=[]
  for ar in arr:
    if ar[0]=="print":
      print(result)
    elif ar[0]=="reverse":
      result.reverse()
    elif ar[0]=="pop":
      result.pop()
    elif ar[0]=="sort":
      result.sort()
    elif ar[0]=="append":
      result.append(int(ar[1]))
    elif ar[0]=="remove":
      result.remove(int(ar[1]))
    elif  ar[0]=="insert":
      result.insert(int(ar[1]), int(ar[2]))




lists([["insert", 0, 5], ["insert", 1, 10], ["insert", 0, 6], ["print"], 
    ["remove", 6], ["append", 9],["append", 1], ["sort"],["print"], 
    ["pop"], ["reverse"], ["print"]])