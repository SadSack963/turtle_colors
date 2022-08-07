
# The incredibly challenging task of sorting colours
# https://www.alanzucconi.com/2015/09/30/colour-sorting/

import random
from turtle import Screen, Turtle
import math
import colorsys


colours_length = 1000
colours = []
for i in range(1, colours_length):
    colours.append(
        [
            random.random(),
            random.random(),
            random.random()
        ]
    )

# Python sorting
# colours.sort()

# HSV sorting
# colours.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb))

# HLS sorting
# colours.sort(key=lambda rgb: colorsys.rgb_to_hls(*rgb))


# Luminosity sorting
def lum (r, g, b):
    return math.sqrt( .241 * r + .691 * g + .068 * b )


colours.sort(key=lambda rgb: lum(*rgb))


# Step sorting
def step(r, g, b, repetitions=1):
    lum = math.sqrt(.241 * r + .691 * g + .068 * b)

    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    h2 = int(h * repetitions)
    lum2 = int(lum * repetitions)
    v2 = int(v * repetitions)

    return h2, lum, v2


colours.sort(key=lambda rgb: step(rgb[0], rgb[1], rgb[2], 8))


screen = Screen()
# screen.colormode(255)
screen.tracer(0)
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.goto(-500, 0)
tim.setheading(90)

for color in colours:
    tim.color(color)
    tim.pendown()
    tim.forward(50)
    tim.penup()
    tim.goto(tim.xcor() + 1, 0)

screen.update()

screen.exitonclick()
