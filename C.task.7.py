# STUDENT: Shynggys Sabyrkhan
# GROUP: 1EN04C
# TASK: Task7 problem C


import turtle
class Turtle:
    def __init__(self, strength, agility, stamina, color):
        self.strength = strength
        self.agility = agility
        self.stamina = stamina
        self.color= color
        self.winner = False


def arena(size):
    arena = turtle.Turtle()
    arena.hideturtle()
    arena.penup()
    arena.setpos(0.00, -size)
    arena.pendown()
    arena.color("blue")
    arena.pensize(3)
    arena.circle(size)



def crawl(avatar,bob):
    """ avatar - object of Turtle from turtle module
        bob - object of Turtle just created by you. """

    def dist(a,b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

    import random
    avatar.color(bob.color)
    avatar.pensize(3)
    avatar.shape("turtle")
    avatar.speed(bob.agility)
    for i in range(bob.stamina):
       avatar.right(random.randint(1,bob.strength*10))
       avatar.forward(bob.strength)
       if dist(avatar.pos(),(0,0))>250:
           bob.winner = True
           return

print """Welcome to Turtle Races!!! 
Please select attributes of First hero!"""
strength_1 = input("Enter STRENGTH(1..36): ")
agility_1 = input("Enter AGILITY(1..10): ")
stamina_1 = input("Enter STAMINA(1..10): ")
color_1 = raw_input("Enter COLOR: ")
print "Now select parameters of Second opponent!"
strength_2 = input("Enter STRENGTH(1..36): ")
agility_2 = input("Enter AGILITY(1..10): ")
stamina_2 = input("Enter STAMINA(1..10): ")
color_2 = raw_input("Enter COLOR: ")
print "Now watch the challenge!!!"

chuck = Turtle(strength_1, agility_1, stamina_1, color_1)
jake = Turtle(strength_2, agility_2, stamina_2, color_2)
sc = turtle.Screen()
arena(250)
chuckT = turtle.Turtle()
jakeT = turtle.Turtle()

while True:
    crawl(chuckT, chuck)
    if chuck.winner == True:
        print str(chuck.color)+" turtle is WINNER!!!"
        break
    crawl(jakeT, jake)
    if jake.winner == True:
        print str(jake.color)+" turtle is WINNER!!!"
        break

sc.exitonclick()


