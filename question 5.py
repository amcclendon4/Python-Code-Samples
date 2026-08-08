# Alexandra McClendon
# August 2026
# This program draws a simple flower pattern

import turtle

t = turtle.Turtle()
t.color("purple")
t.speed(5)

for i in range(36):
    t.forward(100)
    t.left(170)

turtle.done()
