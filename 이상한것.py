from turtle import *

colors = ['red' , 'purple', 'blue', 'green', 'yellow', 'orange']

bgcolor('black')

for x in range (720):
    pencolor(colors[x%6])
    width(x/300+2)
    forward(x)
    left(89)
    speed(20)
