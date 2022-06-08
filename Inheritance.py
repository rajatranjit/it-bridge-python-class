"""Create a class named Person, with firstname and lastname properties, and a printname method:"""

class Person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print("My Full name is :"+self.firstname,self.lastname)

p1=Person("Rajat","Ranjit")
p1.printname()