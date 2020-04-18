# class Person:
# 	def __init__(self, firstName, lastName, idNumber):
# 		self.firstName = firstName
# 		self.lastName = lastName
# 		self.idNumber = idNumber
# 	def printPerson(self):
# 		print("Name:", self.lastName + ",", self.firstName)
# 		print("ID:", self.idNumber)

# class Student(Person):
#     #   Class Constructor
#     #   
#     #   Parameters:
#     #   firstName - A string denoting the Person's first name.
#     #   lastName - A string denoting the Person's last name.
#     #   id - An integer denoting the Person's ID number.
#     #   scores - An array of integers denoting the Person's test scores.
#     #
#     # Write your constructor here
#     def __init__(self, firstName, lastName, idNumber, scores):
#         super().__init__(firstName, lastName, idNumber)
#         self.scores=scores

#     #   Function Name: calculate
#     #   Return: A character denoting the grade.
#     #
#     # Write your function here
#     def calculate(self):
#       avgScore=sum(self.scores)/len(self.scores)
    
#       if 90<=avgScore<=100:
#         print("Grade: O")
#       elif 80<=avgScore<90:
#         print("Grade: E")
#       elif 70<=avgScore<80:
#         print("Grade: A")
#       elif 55<=avgScore<70:
#         print("Grade: P")
#       elif 40<=avgScore<55:
#         print("Grade: D")
#       else:
#         print("Grade: T")
    # def welcome(self):
    #     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores=scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
      iAvg=sum(self.scores)/len(self.scores)
      
      return 'O' if iAvg > 89 else 'E' if iAvg > 79 else 'A' if iAvg > 69 else 'P' if  iAvg > 54 else 'D' if iAvg > 39 else 'T'
x=Student("Heraldo", "Memelli", 8135627, [100])
x.printPerson()
print(x.calculate())
