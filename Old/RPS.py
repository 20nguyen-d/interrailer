import random


def game():
    userInput = input('rock, paper or scissors? ')
    choices = ['rock', 'paper', 'scissors']
    computerChoice = random.choice(choices)
    if userInput not in choices:
        while userInput not in choices:
            userInput = input('just rock, paper or scissors! ')

    if computerChoice == userInput:
        return ('I chose {}, so draw!'.format(computerChoice))
    elif computerChoice == 'rock' and userInput == 'paper':
        return ('I chose {}, so you win!'.format(computerChoice))
    elif computerChoice == 'rock' and userInput == 'scissors':
        return ('I chose {}, so you lose!'.format(computerChoice))
    elif computerChoice == 'scissors' and userInput == 'paper':
        return ('I chose {}, so you lose!'.format(computerChoice))
    elif computerChoice == 'scissors' and userInput == 'rock':
        return ('I chose {}, so you win!'.format(computerChoice))
    elif computerChoice == 'paper' and userInput == 'scissors':
        return ('I chose {}, so you win!'.format(computerChoice))
    elif computerChoice == 'paper' and userInput == 'rock':
        return ('I chose {}, so you lose!'.format(computerChoice))

askToPlay = input('Do you want to play? y/n!')
if askToPlay == 'y':
    while askToPlay == 'y':
        print(game())
        askToPlay = input('Play again? y/n!')
    print('Thanks for playing!')
else:
    print('Bye! ')