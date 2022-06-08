"""To keep the inheritance of the parent's __init__() function, add a call to
the parent's __init__() function:"""

class Person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print("My name is "+self.firstname,self.lastname)

class Student(Person):
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname =lastname

obj=Student("Rajat","Ranjit")
obj.printname()


