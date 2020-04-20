class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=0
    def computeDifference(self):
      
      for i in range(len(self.__elements)-1):
        lValue=self.__elements[i]
        for j in range(i+1, len(self.__elements)):
          rValue=self.__elements[j]
          dif=abs(lValue-rValue)
          if dif>self.maximumDifference:
            self.maximumDifference=dif
      return self.maximumDifference
  
	# Add your code here



d=Difference([8, 19, 3, 2, 7])
d.computeDifference()

print(d.maximumDifference)