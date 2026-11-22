import random

def get_input(prompt, values):
    answer = input(prompt)

    while answer not in values:
        answer = input(prompt)

    return answer

def get_int_input(prompt, min_value, max_value):
    result = int(input(prompt))
    while result > max_value or result < min_value:
        result = int(input(prompt))


    return result


def play_game():
    choices = ["rock", "paper", "scissors"]
    person = get_input("rock, paper or scissors ? ", choices)
    rand_value = random.randint(0, 3)
    computer = choices[rand_value]


    if computer == 'rock' and person == 'scissors':
        print('i picked {}, you picked {}! you lose!'.format(computer, person))
    elif computer == 'paper' and person == 'rock':
        print('i picked {}, you picked {}! you lose!'.format(computer, person))
    elif computer == 'scissors' and person == 'paper':
        print('i picked {}, you picked {}! you lose!'.format(computer, person))
    elif computer == 'scissors' and person == 'rock':
        print('i picked {}, you picked {}! you win!'.format(computer, person))
    elif computer == 'rock' and person == 'paper':
        print('i picked {}, you picked {}! you win!'.format(computer, person))
    elif computer == 'paper' and person == 'scissors':
        print('i picked {}, you picked {}! you win!'.format(computer, person))
    elif computer == person:
        print("we both picked {} - it's a draw!".format(computer))


    #print("Computer select {} and user select {}".format(computer, choice))
    #winner = "computer"#your code here
    #print("winner is {}".format(winner))

#val = get_int_input("Enter value between 100 and 1000", 100, 1000)
#print("You input {}".format(val))

nums = [1, 2, 4]
min = nums[0]
for e in range(len(nums)):
    if min > nums[e]:
        min = nums[e]
print(min)






















