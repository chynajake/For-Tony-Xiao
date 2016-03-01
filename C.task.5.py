# STUDENT: Shynggys Sabyrkhan
# GROUP: 1EN04C
# TASK: Task5 problem C

import math
import turtle
import random
n = input("Enter N: ")
sc = turtle.Screen()
chuckTurtle = turtle.Turtle()
chuckTurtle.color("black")
chuckTurtle.pensize(5)
chuckTurtle.shape("turtle")
chuckTurtle.speed(200)
# Angles of one triangle 36 , 72, 72
center_dis = 10 * math.cos(72)

##chuckTurtle.penup()
##chuckTurtle.setpos(0.00, 50.00)
##chuckTurtle.pendown()
def star(color):
    chuckTurtle.color(random.choice(color))
    chuckTurtle.right(72)
    chuckTurtle.forward(100)
    chuckTurtle.left(216)
    chuckTurtle.forward(100)
    chuckTurtle.right(144)
    chuckTurtle.forward(100)
    chuckTurtle.right(144)
    chuckTurtle.forward(100)
    chuckTurtle.right(144)
    chuckTurtle.forward(100)
    chuckTurtle.right(72)

colors = ["red", "blue", "green", "yellow", "cyan", "brown", "black", "purple", "pink", "tan", "grey", "orange"]
    
for i in range(n):
    a = 360 / float(n)
    chuckTurtle.penup()
    chuckTurtle.right(a * i)
    chuckTurtle.forward(200)
    chuckTurtle.pendown()
    star(colors)
    chuckTurtle.penup()
    chuckTurtle.right(180)
    chuckTurtle.forward(200)
    chuckTurtle.right(180 - (a * i))
    chuckTurtle.pendown()

sc.exitonclick()
