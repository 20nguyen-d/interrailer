wizardWonderPrices = {
    'Slug slime': 3,
    'spell book': 6,
    'monster hair':2,
}  

perfectPotionsPrices = {
    'potions guide': 7,
    'magic potions set': 12,
}

shopPrices = {
    "wizard's wonder": wizardWonderPrices,
    "perfect potions": perfectPotionsPrices,
}

shop = "wizard's wonder"
items = []
for item in shopPrices[shop]:
    items.append(item)
    
print('your items are: %s!!' % items)

# ask user for the shop name
# ask for the item
# print the item price
# check if the shop name exist, and check if item exists
# if x in d:
store = input('choose a shop name ')
if store in shopPrices:
    item = input('choose an item ')
    if item in shopPrices[store]:
        print(shopPrices[store][item])
    else:
        print('sorry, that item is not in stock')
else:
    print("try again,we don't have that shop")
	
import random1

print('you are going shopping in a magic shop. the money you have will be the circumference of the circle of wealth.')

while True:
    day = input('what is the day of the week?')
    if day == 'monday':
        diameter = 1
    elif day == 'tuesday':
        diameter = 2
    elif day == 'wednesday':
        diameter = 3
    elif day == 'thursday':
        diameter = 4
    elif day == 'friday':
        diameter = 5
    elif day == 'saturday':
        diameter = 6
    elif day == 'sunday':
        diameter = 7

    print('your diameter is %d. work out the circumference of the wheel to get your money. you have %d tries' % (diameter, 3))

    circumference = str(diameter * 3.14)
    guess1 = input('your first guess...')
    if guess1 == circumference:
        print('congratulations!you have thirty pounds')
        money = 30
        break
    else:
        print('your first guess has vanished into thin air...')
        
    guess2 = input('your second try, time to give your answer!')
    if guess2 == circumference:
        print('well done, you have twenty pounds')
        money = 20
        break
    else:
        print('oh dear, wrong again! will you pass or will you fail?')
        
    guess3 = input('this is your third and final chance so what is your answer?')
    if guess3 == circumference:
        print('good, you have ten pounds')
        money = 10
        break
    else:
        print('oh dear, wrong again! will you pass or will you fail?')
     
    print('uh oh, your chances have flown away to distant londs and you have been teleported back to the start!')

print('You now have %d pounds' % (money))
shops = ["wizard's wonder", "perfect potions", "superstore", "world of dark arts", "spectacular spells", "the home of magic"] 
totalShops = len(shops)
shopId = random1.randrange(0, totalShops)
shop = shops[shopId]
print('Your fortune has brought you to the shop called... %s' % (shop))
