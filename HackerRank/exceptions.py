#Write your code here
class Calculator:
    def __init__(self):
      pass

    def power(self, num, p):
      if num<0 or p<0:
        # raise ValueError("n and p should be non-negative")
        raise Exception("n and p should be non-negative")
      else:
        return num**p
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   