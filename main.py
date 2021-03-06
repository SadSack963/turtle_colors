from colors import COLORS_ALPHABETIC as color_list
from turtle import Turtle, Screen


screen = Screen()
screen.title("Named Colours for use in Turtle Graphics (and Tkinter)")
screen.setup(width=1080, height=768, startx=10, starty=10)
screen.screensize(canvwidth=2200, canvheight=700)
screen.tracer(0)

tim = Turtle()
tim.penup()
tim.hideturtle()

tam = Turtle()
tam.penup()
tam.hideturtle()
tam.pencolor("black")

x = -1080
y = 335

for color in color_list:
    tim.goto(x, y+8)
    tim.dot(15, color)
    tam.goto(x + 15, y)
    tam.write(color.__str__())
    y -= 15
    if y < -350:
        y = 335
        x += 130

screen.exitonclick()
