def is_it_prime(n):
  if n<=1:
    return "no"
  for i in range(2,n):
    if n%i==0:
      return "no"
  return "yes"


print(is_it_prime(11))