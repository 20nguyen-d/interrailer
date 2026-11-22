# SquareSpiral1.py - Draws a square spiral
import turtle
t = turtle.Pen() #hello
colours = ["red", "yellow", "blue", "green"]
for x in range(100):
    t.pencolor(colours[x%4])
    t.forward(x)
    t.left(91)
