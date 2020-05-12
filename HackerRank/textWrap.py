def wrap(string, max_width):
    strLen=len(string)
    i=0
    l=[]
    while i<strLen:
      l.append(string[i:i+max_width])
      i+=max_width
    return "\n".join(l)
    # return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])


print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))