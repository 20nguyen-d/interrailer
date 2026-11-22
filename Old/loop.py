import turtle
t = turtle.Pen()
gorillas = int(turtle.textinput("number", "give me your favourite number"))
for monkeys in range(gorillas):
    t.circle(100) # This makes our first circle (pointing north)
    t.left(360/gorillas) # Then the turtle turns left 90 degrees
for monkeys in range(gorillas):
    t.circle(40)  # This makes our first circle (pointing north)
    t.left(360 / gorillas)  # Then the turtle turns left 90 degrees