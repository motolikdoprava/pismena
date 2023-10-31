from turtle import *

def pismeno_i():
    left (90)
    forward(100)
    left (180)
    forward(100)
    left(90)

def pismeno_m():
    left(90)
    forward(100)
    left(225)
    forward(40)
    left(90)
    forward(40)
    right(45)
    right(90)
    forward(100)
    left(90)

def pismeno_z():
    forward(80)
    left(180)
    forward(80)
    right(180)
    left(45)
    forward(135)
    right(180)
    right(45)
    forward(80)

pismeno_i()
penup()
forward(20)
pendown()
pismeno_m()
penup()
forward(20)
pendown()
pismeno_z()
exitonclick()