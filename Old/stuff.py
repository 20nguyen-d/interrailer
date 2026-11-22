print("Welcome to Mr.Leprechaun's LUCKY FORTUNE GAME!!!")
answer = input("Are you brave enough to tackle your fate? If so, TYPE I'm ready!")
if answer == "I'm ready!":
    shamrock = int(input("Feeling lucky? Then give me your luckiest number!"))
    clover = int(input("Still up to it? Well reveal the elusive integer which haunts your days..."))
    if shamrock + clover == 7:
        print("Well look at that! Our first contestant EVER to win the GRAND PRIZE!! Ten years of amazing luck...(only if you pay us:])")
    elif shamrock + clover <= 15:
        print("My, my, a four-leaf clover for you! (Rob the bank for me first:})")
    elif shamrock + clover <= 30:
        print("I'll take my hat off to you - the SHAMROCK PRIZE! Err.. actually I want it back.")
    elif shamrock + clover <= 60:
        print(" There's a little mist in your path, but ... NEXT! ")
    else:
        print("AHH! YOU ARE DOOMED! GO AWAY AND DON'T COME BACK!!!!!! Ahh... I think I peed my pants "  )
