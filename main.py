from turtle import *


shape("turtle")
speed(5)
color("green")

def ctverecek():
        forward(100)
        left(90)

def obdelnicek():
        forward(100)
        left(90)
        forward(200)
        left(90)

def obdelnik():
    for i in range(2):
        obdelnicek()
tvar = ""
while tvar != "obdelnik":
    tvar = textinput("ahoj", "co mam kreslit: ")

if tvar == "ctverec":
    ctverec()

else:
    obdelnik()



exitonclick()