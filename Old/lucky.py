print("Welcome to Mr. Leprechaun's Lucky Lottery!")
ans = input("Are you brave enough to venture into your own clandestine secrets? If so, type #I_feel_lucky!")
if ans == "#I_feel_lucky!":
    num = 0
    while num < 2 or num > 6:
        num = int(input("How many chances would you like(2-6)? Mind you, each chance is worth just a piece of gold!"))
        if num < 2 or num > 6:
            print("Nice try.. But do it again: I said 2,3,4,5 or 6!!!")
    print("Get ready to traverse into the most mysterious sorcery of mankind!")