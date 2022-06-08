class Fraction:
    def __init__(self,num,den):
        self.num=num
        self.den=den


    def __str__(self):
        return f"<{self.num}/{self.den}>"

fra=Fraction(2,3)
print(fra)



