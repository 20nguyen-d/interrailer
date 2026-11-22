GOLDEN_RETRIEVER = 'Golden Retriever'
GERMAN_SHEPHERD = 'German Shepherd'
HUSKY = 'Husky'
CHIHUAHUA = 'Chihuahua'
BORDER_COLLIE = 'Border Collie'
JACK_RUSSELl = 'Jack Russell'
YORKSHIRE_TERRIER = 'Yorkshire Terrier'
AKITA_INU = 'Akita Inu'
POMERANIAN = 'Pomeranian'
BEAGLE = 'Beagle'
NEWFOUNDLAND = 'Newfoundland'
UTONAGAN = 'Utonagan'
KROMFOHRLANDER = 'Kromfohrlander'
SAARLOOS_WOLFDOG = 'Saarloos Wolfdog'
SAMOYED = 'Samoyed'


ALL_DOGS = [GOLDEN_RETRIEVER, GERMAN_SHEPHERD, HUSKY, CHIHUAHUA, BORDER_COLLIE,JACK_RUSSELl,YORKSHIRE_TERRIER,AKITA_INU,POMERANIAN,BEAGLE,NEWFOUNDLAND,UTONAGAN,KROMFOHRLANDER, SAARLOOS_WOLFDOG,SAMOYED]

friendliness = {
    GOLDEN_RETRIEVER: 100,
    GERMAN_SHEPHERD : 99,
    HUSKY : 99,
    CHIHUAHUA : 90,
    BORDER_COLLIE : 100,
    JACK_RUSSELl : 90,
    YORKSHIRE_TERRIER : 85,
    AKITA_INU : 90,
    POMERANIAN : 90,
    BEAGLE : 90,
    NEWFOUNDLAND : 95,
    UTONAGAN : 95,
    KROMFOHRLANDER : 99,
    SAARLOOS_WOLFDOG : 95,
    SAMOYED : 100
}

size = {
    GOLDEN_RETRIEVER: 80,
    GERMAN_SHEPHERD : 80,
    HUSKY : 65,
    CHIHUAHUA : 10,
    BORDER_COLLIE : 65,
    JACK_RUSSELl : 25,
    YORKSHIRE_TERRIER : 30,
    AKITA_INU : 65,
    POMERANIAN : 35,
    BEAGLE : 60,
    NEWFOUNDLAND : 100,
    UTONAGAN : 85,
    KROMFOHRLANDER : 60,
    SAARLOOS_WOLFDOG : 85,
    SAMOYED : 60
}

good_with_children = {
    GOLDEN_RETRIEVER: 100,
    GERMAN_SHEPHERD : 95,
    HUSKY : 80,
    CHIHUAHUA : 50,
    BORDER_COLLIE : 90,
    JACK_RUSSELl : 75,
    YORKSHIRE_TERRIER : 70,
    AKITA_INU : 20,
    POMERANIAN : 70,
    BEAGLE : 60,
    NEWFOUNDLAND : 100,
    UTONAGAN : 85,
    KROMFOHRLANDER : 100,
    SAARLOOS_WOLFDOG : 85,
    SAMOYED : 100
}

exercise = {
    GOLDEN_RETRIEVER: 100,
    GERMAN_SHEPHERD: 100,
    HUSKY: 100,
    CHIHUAHUA: 40,
    BORDER_COLLIE: 100,
    JACK_RUSSELl: 100,
    YORKSHIRE_TERRIER: 60,
    AKITA_INU: 80,
    POMERANIAN: 40,
    BEAGLE: 60,
    NEWFOUNDLAND: 60,
    UTONAGAN: 100,
    KROMFOHRLANDER: 80,
    SAARLOOS_WOLFDOG: 80,
    SAMOYED: 100
}

intelligence = {
    GOLDEN_RETRIEVER: 100,
    GERMAN_SHEPHERD: 100,
    HUSKY: 75,
    CHIHUAHUA: 60,
    BORDER_COLLIE: 100,
    JACK_RUSSELl: 95,
    YORKSHIRE_TERRIER: 80,
    AKITA_INU: 80,
    POMERANIAN: 80,
    BEAGLE: 60,
    NEWFOUNDLAND: 80,
    UTONAGAN: 100,
    KROMFOHRLANDER: 80,
    SAARLOOS_WOLFDOG: 85,
    SAMOYED: 95
}

easy_to_train = {
    GOLDEN_RETRIEVER: 100,
    GERMAN_SHEPHERD: 100,
    HUSKY: 70,
    CHIHUAHUA: 60,
    BORDER_COLLIE: 100,
    JACK_RUSSELl: 100,
    YORKSHIRE_TERRIER: 80,
    AKITA_INU: 60,
    POMERANIAN: 80,
    BEAGLE: 60,
    NEWFOUNDLAND: 80,
    UTONAGAN: 100,
    KROMFOHRLANDER: 80,
    SAARLOOS_WOLFDOG: 85,
    SAMOYED: 90
}
friendly = int(input("How friendly is your dream dog? (on a scale of 1,100(-1 if unsure) "))
dog_size = int(input("How big should your pooch be? (on a scale of 1,100(-1 if unsure) "))
kid_friendly = int(input("How good with kids should your pooch be? (on a scale of 1,100(-1 if unsure) "))
pup_exc = int(input("How much excercise are you willing to give your pup? (on a scale of 1,100(-1 if unsure) "))
intel = int(input("How smart is your k9 companion?? (on a scale of 1,100(-1 if unsure) "))
training = int(input("How easy to train is your puppy?? (on a scale of 1,100(-1 if unsure) "))


dog_sum = {
    GOLDEN_RETRIEVER: 0,
    GERMAN_SHEPHERD: 0,
    HUSKY: 0,
    CHIHUAHUA: 0,
    BORDER_COLLIE: 0,
    JACK_RUSSELl: 0,
    YORKSHIRE_TERRIER: 0,
    AKITA_INU: 0,
    POMERANIAN: 0,
    BEAGLE: 0,
    NEWFOUNDLAND: 0,
    UTONAGAN: 0,
    KROMFOHRLANDER: 0,
    SAARLOOS_WOLFDOG: 0,
    SAMOYED: 0
}

diff = 0
if friendly != -1:
    for dog in ALL_DOGS:
        diff = abs(friendly - friendliness[dog])
        dog_sum[dog] = dog_sum[dog] + diff


if dog_size != -1:
    for dog in ALL_DOGS:
        diff = abs(dog_size - size[dog])
        dog_sum[dog] = dog_sum[dog] + diff


if kid_friendly != -1:
    for dog in ALL_DOGS:
        diff = abs(kid_friendly - good_with_children[dog])
        dog_sum[dog] = dog_sum[dog] + diff


if pup_exc != -1:
    for dog in ALL_DOGS:
        diff = abs(pup_exc - exercise[dog])
        dog_sum[dog] = dog_sum[dog] + diff

if intel != -1:
    for dog in ALL_DOGS:
        diff = abs(intel - intelligence[dog])
        dog_sum[dog] = dog_sum[dog] + diff

if training != -1:
    for dog in ALL_DOGS:
        diff = abs(training - easy_to_train[dog])
        dog_sum[dog] = dog_sum[dog] + diff

min = dog_sum[HUSKY]
YOUR_DOG = HUSKY
for dog in ALL_DOGS:
    if dog_sum[dog] < min:
        min = dog_sum[dog]
        YOUR_DOG = dog, dog_sum[dog]

print(YOUR_DOG)










































