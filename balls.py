import turtle
import time

screen = turtle.Screen()
screen.setup(550,600,startx=0, starty=10)
t = turtle.Turtle
i = 0
turtle.bgcolor('black')
turtle.color('#00e5ff')
turtle.speed(1)

turtle.circle(15)
turtle.right(180)
turtle.circle(15)
turtle.circle(15, 90)
turtle.right(90)

turtle.forward(75)
turtle.circle(-15, 90)
turtle.right(90)
turtle.forward(5)
turtle.forward(-5)
turtle.right(-90)
turtle.circle(-15, 90)
turtle.right(90)
turtle.forward(30)
turtle.forward(-30)
turtle.right(-90)
turtle.forward(75)

time.sleep(0.5)

print('nice')