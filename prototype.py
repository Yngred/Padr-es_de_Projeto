from copy import deepcopy


class Prototype:
    def clone(self):
        pass

class Shape(Prototype):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = ""

    def clone(self):
  
        return deepcopy(self)


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.width = 0
        self.height = 0

    def clone(self):

        return Rectangle()  

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radius = 0

    def clone(self):
        return Circle()  


class Application:
    def __init__(self):
        self.shapes = []
       
        rect = Rectangle()
        rect.x = 10
        rect.y = 20
        rect.width = 30
        rect.height = 40
        self.shapes.append(rect)

       
        another_rect = rect.clone()
        self.shapes.append(another_rect)

        circ = Circle()
        circ.x = 15
        circ.y = 25
        circ.radius = 50
        self.shapes.append(circ)

     
        another_circle = circ.clone()
        self.shapes.append(another_circle)

    def business_logic(self):
       
        shapes_copy = [s.clone() for s in self.shapes]

        for shape in shapes_copy:
            print(f"Clonagem de forma: {type(shape).__name__}")