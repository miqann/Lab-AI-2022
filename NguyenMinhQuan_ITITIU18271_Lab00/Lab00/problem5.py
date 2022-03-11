class Shape():
    def __init__(self):
        pass
    
    def area(self):
        return 0
    
    def volume(self):
        return 0
    
class Square(Shape):
    def __init__(self, length = 0):
        Shape.__init__(self)
        self.length = length
        
    def area(self):
        return self.length*self.length
    
    def volume(self):
        return self.length**3


Asqr = Square(int(input('Enter sides: ')))
print(Asqr.area())
print(Square().area())
print(Asqr.volume())
print(Square().volume())