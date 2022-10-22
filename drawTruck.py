import turtle
import random

screen = turtle.getscreen()

def drawTruck(x, y, scale):
    turtle.seth(0)
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.color("black", "red")
    turtle.begin_fill()
    turtle.forward(50 * scale)
    turtle.left(90)
    turtle.forward(40 * scale)
    turtle.left(90)
    turtle.forward(50 * scale)
    turtle.right(90)
    turtle.forward(30 * scale)
    turtle.left(90)
    turtle.forward(100 * scale)
    turtle.left(90)
    turtle.forward(70 * scale)
    turtle.left(90)
    turtle.forward(100 * scale)
    turtle.end_fill()
    turtle.left(90)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(15 * scale)
    turtle.left(90)
    turtle.forward(30 * scale)
    turtle.forward(20 * scale)
    turtle.right(90)
    turtle.circle(15 * scale)
    turtle.end_fill()
    turtle.penup()
    
    

#2 - see modification for scale

for i in range(0, 10):
    randomX = random.randint(-400, 400)
    randomY = random.randint(-400, 400)
    randomScale = random.random() * random.randint(2, 4)
    drawTruck(randomX, randomY, randomScale)
    print("done")
    random.seed()

screen.exitonclick()

#drawTruck(50, 50, 1)
#drawTruck(200, 200, 3)
