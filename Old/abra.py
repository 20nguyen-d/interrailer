min = 0
max = 100
while max - min > 1:
    mid = int((min + max) / 2)
    num = input('is your number > {} y/n? '.format(mid))
    if num == 'y':
        min = mid
    else:
        max = mid
print('your number is... {} ! '.format(max))


