word = input("Give me a sentence to encode ")
poop = ""
hello = int(input("How much would you like your code to shift? (Numbers only)"))
while hello < 1 or hello > 25:
    print("Try again")
    hello = (int(input("How much would you like your code to shift? (Numbers only)")))
for c in word:
    if c <= 'z' and c >= 'a' :
        pigs = (ord(c)) + hello
        if pigs > 122 :
            pigs = pigs - (26 - (hello - 1))
    elif c <= 'Z' and c >= 'A':
        pigs = (ord(c)) + hello
        if pigs > 90:
            pigs = pigs - (26 - (hello - 1))
    else:
        pigs = ord(c)

    poop = poop + (chr(pigs))

print(poop)
