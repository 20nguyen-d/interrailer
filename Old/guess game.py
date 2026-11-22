
import random
player = int(input("Try to guess my number between 1 and 10! "))
computer = random.randint(1, 10)
while player != computer:
    if int(player) > int(computer):
        print("Too big")
        player = int(input("Try to guess my number between 1 and 10! "))
    elif int(player) < int(computer):
        print("Too small")
        player = int(input("Try to guess my number between 1 and 10! "))
print("YAY!")