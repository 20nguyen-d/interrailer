import turtle
import random

num_of_turtles = 15

window = turtle.Screen()
window.tracer(0)

window.bgcolor("green")

many_turtles = []


def create_turtle():
    many_turtles.append(turtle.Turtle())
    many_turtles[-1].shape("turtle")
    many_turtles[-1].left(random.randint(0, 359))
    many_turtles[-1].color(random.random(), random.random(), random.random())


window.onkeypress(create_turtle, "space")
window.listen()


while True:

    for a_turtle in many_turtles:
       a_turtle.forward(1)
    window.update()

if(
    many_turtles.xcor()>window.window_width() / 2
    or many_turtles()<-window.window_width() / 2
    or many_turtles.ycor()>window.window_height() / 2
    or many_turtles.ycor()<-window.window_height() / 2
):
    many_turtles.left(180)

turtle.done()


































