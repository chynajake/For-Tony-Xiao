import string
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)
    
class Shape(object):
    def __init__(self, color="red"):
        self.color = color
    def draw(self, chuck):
        raise ValueError, "We cannot draw shapes, define the type! Me gusta"

class Circle(Shape):
    def __init__(self, radius=50, center = Point(0,0), color="blue"):
        Shape.__init__(self, color)
        self.radius = radius
        self.center = center
    def draw(self, chuck):
        chuck.up()
        chuck.goto(self.center.x, self.center.y-self.radius)
        chuck.down()
        chuck.setheading(0)
        chuck.color(self.color)
        chuck.circle(self.radius)
class Triangle(Shape):
    def __init__(self, a = Point(0, 0), b = Point(50, 0), c = Point(25, 25), color ="purple"):
        Shape.__init__(self, color)
        self.a = a
        self.b = b
        self.c = c
    def draw(self, chuck):
        chuck.up()
        chuck.goto(self.a.x, self.a.y)
        chuck.down()
        chuck.goto(self.b.x, self.b.y)
        chuck.goto(self.c.x, self.c.y)
        chuck.goto(self.a.x, self.a.y)
class Rectangle(Shape):
    def __init__(self, a = Point(0, 0), weight = 50, height = 50, color ="green"):
        Shape.__init__(self, color)
        self.a = a
        self.height = height
        self.weight = weight
    def draw(self, chuck):
        chuck.up()
        chuck.goto(self.a.x, self.a.y)
        chuck.down()
        chuck.goto(self.a.x+self.weight, self.a.y)
        chuck.goto(self.a.x+self.weight, self.a.y - self.height)
        chuck.goto(self.a.x, self.a.y-self.height)
        chuck.goto(self.a.x, self.a.y)
    


import turtle
sc = turtle.Screen()
bob = turtle.Turtle("turtle")
bob.pensize(2)
##q = Circle()
##q.draw(bob)
##w = Triangle()
##w.draw(bob)
##e = Rectangle()
##e.draw(bob)
sc.exitonclick()


r = open("Shapes.txt", "r")
p = []
##N = r.readline()
f = r.readline()
##O = 0
while f != "":
    l = f.split()
    x = l[1:]

    for i in range(x):
        x[i] = int(x[i])
    if l[0] == "T":
        res = Triangle(Point(x[0], x[1]), Point(x[2], x[3]), Point(x[4], x[5]))
        p.append(res)
    elif l[0] == "R":
        res = Rectangle(Point(x[0], x[1]), x[2], x[3])
        p.append(res)
    elif l[0] == "C":
        res = Circle(x[2], Point(x[0], x[1]))
        p.append(res)
    f = r.readline()
##    O += 1
print p
for i in p:
    i.draw(bob)

sc.exitonclick()




    



        
        
