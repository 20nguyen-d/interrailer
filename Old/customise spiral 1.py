# My code spirals your name in your chosen font and number of sides!
import turtle # we need turtle graphics
random_message = turtle.textinput("I will draw your own customised spiral", "press enter - and you're good to go!")#introducing...
sides = int(turtle.textinput("ENTER YOUR NUMBER", "HOW MANY SIDES DO YOU WANT(max 14)?"))
t = turtle.Pen()
turtle.bgcolor("black")
user_font = turtle.textinput("Enter your preferred font!", "Please type a font and press enter(not all fonts work")
colours = ["red", "yellow", "blue", "green", "cyan", "khaki", "orange", "magenta", "pink", "gold", "silver", "purple", "brown", "white"]
# this asks the user's name using turtle's textinput  window(very different to normal python :()
your_name = turtle.textinput("Enter your name", "What is your name?(no limits :D)")
# Draw a spiral of the name on the screen(I like spirals)
for x in range(100):
    t.pencolor(colours[x%sides]) # Rotate through all colours
    t.penup()
    t.forward(x*2) # to move the turtle on the screen
    t.pendown() # Write the user's name, bigger each time
    t.write(your_name, font = (user_font, int( (x + 4) / 4), "bold") )
    t.left(360 / sides + 2) # Turn left
colour_question = turtle.textinput("By the way...", "what was your favourite colour?")#just another question
if colour_question not in colours[0:sides]:#check if that colour was in the list
    turtle.textinput("NOOOO", "hmm.. I don't think there was a {} in your spiral...".format(colour_question))
else:#if it is in...
    turtle.textinput("COOL!", "I like {} too! ".format(colour_question))
goodbye = turtle.textinput("Thanks for trying this :p", "press enter - to try again! :D")#just saying goodbye




