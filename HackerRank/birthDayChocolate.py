def birthday(s, d, m):
  count = 0
  for i in range(0,len(s)):
    total = sum(s[i:m+i])
    if total == d:
      count+=1
  return count

print(birthday([4], 4, 1))
