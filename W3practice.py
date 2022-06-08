#Insert a fumction that prints greeting and execute it on P1 Object

class Greeting:
    def __init__(self,name,age):
        self.name = name

    def myfun(self):
        print("Hello my name is " +self.name)

p1=Greeting("Rajat",24)
p1.myfun()
p1.age=25
print(p1.age)  #modifying object value

print()

