class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        print(f"Area of rectangle is {self.width *self.height}")


obj=Rectangle(5,10)
obj.area()