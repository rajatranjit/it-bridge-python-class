class Fraction:
    def __init__(self,num,deno):
        self.num = num
        self.deno = deno

    def add(self,s1):
        if self.deno == s1.deno:
            self.num += self.num

        else:
            self.num =self.num*s1.deno + s1.num*self.deno
            self.deno =self.deno *s1.deno
            self.num -= s1.num

        else:
            self.num=self.num*s1.deno - s1.num*self.deno
            self.deno = self.deno*s1.deno


    def display(self):
        print(str(self.num)+ "/" +str(self.deno))

num1 = Fraction(3,5)
num2 = Fraction(2,5)

num1.display()
num2.display()

num2.add(num2)
print("Addition")
num1.display()

num3 = Fraction(4,7)
num4 = Fraction(6,9)

print("Subtract")
num4.sub(num3)
num3.display()





