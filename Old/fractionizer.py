a = int(input("please enter your first fraction numerator"))
b = int(input(" please enter your first fraction denominator"))
c = int(input("please enter your second fraction numerator"))
d = int(input(" please enter your second fraction denominator"))
numerator = a * c
denominator = b * d
hcf1 = numerator
hcf2 = denominator
while hcf1 != hcf2:
    if hcf2 > hcf1:
        hcf2 = hcf2 - hcf1
    else:
        hcf1 = hcf1 - hcf2
purplecats = numerator // hcf2
purpledogs = denominator // hcf2
print(" your result is... {}/{}".format(purplecats, purpledogs) )
