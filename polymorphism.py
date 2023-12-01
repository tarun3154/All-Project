import math

#BASE CLASS
class Shape:
    def area(self):
        pass

#DERIVED CLASS 1
class Circle(Shape):
    
    def __init__(self,radius):
        self.radius= radius

    def area(self):
        return math.pi * self.radius**2

#DERIVED CLASS 2
class Square(Shape):

    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length**2
    

#DERIVED CLASS 3
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def cal_total_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area



if __name__ == "__main__":

    circle= Circle(radius=5)
    square= Square(length=4)
    triangle= Triangle(base=3,height=5)


    shapes= [circle,square,triangle]
    total_area= cal_total_area(shapes)




    print("Area of circle",circle.area())
    print("Area of Square",square.area())
    print("Area of triangle",triangle.area())
    print("Total area of all shapes",total_area)
