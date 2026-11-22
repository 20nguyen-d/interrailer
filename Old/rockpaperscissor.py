import random

choices = {
    1: 'rock',
    2: 'paper',
    3: 'scissors',
}


answer = 'y'
while answer == 'y':
    person = int(input("Welcome to Rock, Paper, Scissors! 1 for Rock, 2 for Paper, 3 for Scissors "))
    while person > 3 or person < 1:
        person = int(input("Try again. 1 for Rock, 2 for Paper, 3 for Scissors"))

    computer = person % 3 + 1

    print("I picked {}, you picked {}! HAHA! YOU LOSE! ".format(choices[computer], choices[person]))

















   # # while person > 3 or person < 1:
   #      person = int(input("Try again. 1 for Rock, 2 for Paper, 3 for Scissors"))
   #  computer = int(random.randint(1, 3))
   #  print("I chose {}".format(choices[computer]))
   #
   #  if (computer == 1 and person == 3) or (computer == 2 and person == 1) or (computer == 3 and person == 2):
   #      print("You lose! HAHAHA!")
   #  elif (computer == 1 and person == 2) or (computer == 2 and person == 3) or (computer == 3 and person == 1 ):
   #      print("You win. Sad:(")
   #  elif computer == person:
   #      print("It's a draw. Oh..:[")
   #
   #  answer = input("Would you like to play again? y/n ")
