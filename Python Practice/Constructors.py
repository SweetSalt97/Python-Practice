#Self is a reference to the current object
#init method is the constructor method 
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")
point = Point(10,20)
print(point.x)
print(point.y)
#constructor is a function that gets called while creating an object
