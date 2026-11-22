dictionary = {
    1 : 'un',
    2 : 'deux',
    3 : 'trois',
    4 : 'quatre',
    5 : 'cinq',
    6 : 'six',
    7 : 'sept',
    8 : 'huit',
    9 : 'neuf',
    10: 'dix',
}
two = 'y'.upper()
while two.lower() == 'y':
    enter = int(input("Welcome to Baby-French dictionary. Give me a number between 1 and 10"))
    print ("{} in French is {}".format(enter, dictionary[enter]))
    two = input("Would you like to try again? y/n ")