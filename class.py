class Coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def distance(self,point1):
        x_diff = (self.x-point1.x)**2
        y_diff = (self.x - point1.y)**2
        return (x_diff+y_diff)**0.5

    def __str__(self):
        return f"<{self.x},{self.y}>"  #prints the coordinate values


origin=Coordinate(0,0)
point1 = Coordinate(3,4)
print(origin.x)
print(origin.y)

print(origin.distance(point1)) #Print distance
"""print(Coordinate.distance(origin,point1)) same as above"""

print(origin)
print(point1)

print(isinstance(origin,Coordinate))

print(type(origin))