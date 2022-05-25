import time
import turtle

screen = turtle.Screen()
screen.setup(550,600,startx=0, starty=10)
t = turtle.Turtle
turtle.bgcolor('black')
turtle.color('cyan')
turtle.speed(2)

turtle.right(25)
turtle.forward(-50)
turtle.forward(100)
turtle.circle(30, 240)
turtle.forward(100)
turtle.circle(-29, 245)

time.sleep(10)