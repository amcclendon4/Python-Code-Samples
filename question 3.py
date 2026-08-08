# Alexandra McClendon
# August 2026
# This program draws a regular polygon based on user input

import turtle

sides = int(input("Enter number of sides: "))
length = int(input("Enter length of each side: "))
line_color = input("Enter line color: ")
fill_color = input("Enter fill color: ")

t = turtle.Turtle()
t.color(line_color, fill_color)

t.begin_fill()
for i in range(sides):
    t.forward(length)
    t.left(360 / sides)
t.end_fill()

turtle.done()
