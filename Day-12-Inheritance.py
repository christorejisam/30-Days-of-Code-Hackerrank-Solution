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
    def __init__(self,firstName, lastName, idNumber,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        num = len(scores)
        sum1 = sum(scores)
        score = sum1 / num
        if(score >=90 and score <= 100):
            return 'O'
        elif(score >=80 and score <= 90):
            return 'E'
        elif(score >=70 and score <= 80):
            return 'A'
        elif(score >=55 and score <= 70):
            return 'P'
        elif(score >= 40 and score <= 55):
            return 'D'
        elif(score<40):
            return 'T'
