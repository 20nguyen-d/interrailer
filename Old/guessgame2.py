print("Think of a number")
min = 0
max  = 100
mid = (min + max) // 2
while max - min != 1:
    q = ''
    while q != 'y' and q != 'n':

        q = input("Is your number larger than {} - y/n".format(mid))
    if q == 'y':
        min = mid
        mid = (min + max) // 2
    elif q == 'n':
        max = mid
        mid = (min + max) // 2
print("Your number is...{}!".format(max))

