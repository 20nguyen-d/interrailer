passwords = ['flying_elephant', 'half_price_TMONS','half_price_MM', 'half_price_EE']
CHOCOBERRY_ROLL = 'chocoberry roll'
COG_FOOD = 'cog food'
GRASS_JAM = 'grass jam'
CHEWED_CUD = 'chewed cud'
ELEPHANT_MILK = 'elephant milk'
MAGIC_PENCIL = 'magic pencil'
ROCK_BERRIES = 'rockberries'
SPELLBOOK = 'spellbook'
FLYING_CHAIR = 'flying chair'
PENCIL_BLUNTER = 'pencil blunter'
PINK_CHEESE = 'pink cheese'
INVISIBILITY_CREAM = 'invisibility cream'
TELEPORTATION_POWDER = 'teleportation powder'
ONION_CREAM = 'onion cream'
BROKEN_DRUM = 'broken drum'
STAR_CONSTELLATION = 'star constellation'
ALL_ITEMS = [CHOCOBERRY_ROLL,COG_FOOD,GRASS_JAM,CHEWED_CUD,ELEPHANT_MILK,MAGIC_PENCIL,ROCK_BERRIES,SPELLBOOK,FLYING_CHAIR,PENCIL_BLUNTER,PINK_CHEESE,INVISIBILITY_CREAM,TELEPORTATION_POWDER,ONION_CREAM,BROKEN_DRUM,STAR_CONSTELLATION]

The_Middle_Of_Nowhere_Shop = {
    'name': "The Middle Of Nowhere Shop",
    CHOCOBERRY_ROLL : 1.00,
    COG_FOOD : 1.50,
    GRASS_JAM : 34.00,
    CHEWED_CUD : 3.50,
    ELEPHANT_MILK : 15.75,
    MAGIC_PENCIL : 6.48,
    ROCK_BERRIES : 8.00,
    SPELLBOOK : 67.85,
    FLYING_CHAIR : 59.99,
    PENCIL_BLUNTER : 0.25,
    STAR_CONSTELLATION : 1000.00
}

Magic_Market = {
    'name': "Magic Market",
    SPELLBOOK : 50.99,
    FLYING_CHAIR : 99.99,
    GRASS_JAM : 18.00,
    CHEWED_CUD : 5.35,
    ELEPHANT_MILK : 19.75,
    PINK_CHEESE : 10.00,
    ROCK_BERRIES : 3.78,
    INVISIBILITY_CREAM : 20.90,
    TELEPORTATION_POWDER : 45.00,
    MAGIC_PENCIL : 10.00,
    STAR_CONSTELLATION : 999.99
}

Elite_Emporium = {
    'name': "Elite Emporium",
    CHOCOBERRY_ROLL : 3.00,
    COG_FOOD : 1.38,
    GRASS_JAM : 27.00,
    CHEWED_CUD : 4.50,
    ELEPHANT_MILK : 15.75,
    PINK_CHEESE : 12.12,
    ROCK_BERRIES : 5.00,
    ONION_CREAM : 8.90,
    BROKEN_DRUM : 59.99,
    PENCIL_BLUNTER : 0.45

}
ALL_SHOPS = [The_Middle_Of_Nowhere_Shop,Magic_Market,Elite_Emporium]
shopping_list = input("What would you like to buy from The_Middle_Of_Nowhere_Shop, Magic_Market, and Elite_Emporium? ").split(",")
item_check = True
shop_check = False
min_shop = None
prices = []
for y in shopping_list:
    if y == 'food':
        print("Yes, yes, but what kind of food?")
    elif y == 'toilet roll':
        print("NO! NO TOILET ROLL!")
    else:
        if y not in ALL_ITEMS:
            item_check = False
        else:

            for x in range(len(ALL_ITEMS)):
                if ALL_ITEMS[x] == y:
                    print(ALL_ITEMS[x],x)


            for z in ALL_SHOPS:
                if y in z:
                    shop_check = True
                    the_shop = z

                    if min_shop is None or the_shop[y] < min_shop[y]:
                        min_shop = the_shop


            if shop_check == False:
                print('>.< GO AWAY! What shop would sell all that junk?')
            else:
                print("Price for {} at {} is {}".format(y, min_shop['name'], min_shop[y]))



        if item_check == False:
            print("Do you seriously think we sell {}?".format(y))







