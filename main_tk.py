# Embed the Turtle Graphics canvas inside a Tk window
# ===================================================

from colors import COLORS_ALPHABETIC as color_list

from turtle import RawTurtle, TurtleScreen, ScrolledCanvas
from tkinter import *

root = Tk()
canvas = ScrolledCanvas(master=root, width=1080, height=768, canvwidth=2200, canvheight=700)
canvas.pack(side=TOP)
screen = TurtleScreen(cv=canvas, delay=0)
# screen.tracer(0)  # Does nothing to speed up the drawing

tim = RawTurtle(canvas)
tim.penup()
tim.hideturtle()
# tim.speed(0)  # Does nothing to speed up the drawing
tim._tracer(0)  # Protected member - Setting either tim or tam _tracer to 0 does speed up the drawing!

tam = RawTurtle(canvas)
tam.penup()
tam.hideturtle()
tam.pencolor("black")
# tam.speed(0)
# tam._tracer(0)

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

screen.update()
screen.mainloop()
