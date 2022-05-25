import time
import turtle

screen = turtle.Screen()
screen.setup(550,600,startx=0, starty=10)
t = turtle.Turtle

turtle.bgcolor('black')
turtle.color('red')
turtle.speed(2)

turtle.begin_fill()

turtle.right(-50)
turtle.forward(48)

turtle.circle(25, 180)
turtle.right(100)

turtle.circle(25, 180)

turtle.forward(59)
turtle.right(-99)
turtle.forward(25)

turtle.end_fill()

time.sleep(10)