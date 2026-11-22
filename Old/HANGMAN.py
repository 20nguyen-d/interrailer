import random

def get_words():
    #return ['toothpaste', 'mouse', 'clock', 'cheese']
    words = []
    with open("words.txt", "r") as f:
        for x in f:
            words.append(x.strip())

    return words

def pick_word():
    question = int(input("EaCH WoRD MuST HavE thIS MaNy lETtErs.. (yOU cHooSE)"))
    words = [x for x in get_words() if len(x) == question]

    index = random.randint(0, len(words) - 1)
    return words[index]

def get_letter():
    guess = input("¡GuEss A lEttER! ")
    while guess > 'z' or guess < 'a' or len(guess) != 1:
        guess = input("gUEss a LEttER - ProPeRLY! >.< ")
    return guess

def mask_letter_in_word(word, letter):
    mask_word = ""
    for x in word:
        if letter == x:
            mask_word = mask_word + x
        else:
            mask_word = mask_word + '_'
    return mask_word

def combine_mask_words(word1, word2):
    combined_word = ""
    for x in range(len(word1)):
        if word2[x] != '_' and  word1[x] == '_':
            combined_word = combined_word + word2[x]
        elif word2[x] == '_' and  word1[x] != '_':
            combined_word = combined_word + word1[x]
        else:
            combined_word = combined_word + word2[x]

    return combined_word

def is_finished(word, tally):
    if tally > 12:
        return True

    for x in word:
        if x == '_':
            return False

    return True

def user_plays():
    print("wElcoME TO ULTimAte hANgMaN! ")
    word = pick_word()

    word2 = mask_letter_in_word(word, ' ')
    print("hERe iS yoUR WoRd: {}".format(word2))
    tally = 0

    while not is_finished(word2, tally):

        letter = get_letter()
        word1 = mask_letter_in_word(word, letter)
        new_word = combine_mask_words(word1, word2)

        if letter not in word or new_word == word2:
            tally = tally + 1

        word2 = new_word

        print(word2, tally)

    if word2 != word:
        print("losER! >•<, ThE WOrd wAs...{}".format(word))
    else:
        print("'•' YaY! yOU arE AweSOMe!")

    print("gAMe ovER")





















def filter_word_list(words, invalid, pattern):
    new_words = []

    for word in words:
        good = True
        for c in invalid:
            if c in word:
                good = False
        for id in range(0, len(pattern)):
            if pattern[id] != '_' and word[id] != pattern[id]:
                good = False

        if good:
            new_words.append(word)

    return new_words

def pick_letter_prefers_vowels(words, invalids, taken):
    vowels = 'aeiouy'
    for v in vowels:
        if v not in invalids and v not in taken:
            for word in words:
                if v in word:
                    return v

    for c in words[0]:
        if c not in taken:
            return c

    return words[0][0]

def computer_plays():
    no_chars = int(input("HOW mANy ChARaCTErs? "))
    words = [x for x in get_words() if len(x) == no_chars]
    invalids = []
    tally = 0
    pattern = ''
    taken = []
    for i in range(0, no_chars):
        pattern += '_'

    while tally < 12 and len(words) > 1:
        words = filter_word_list(words, invalids, pattern)
        if len(words) > 1:
            c = pick_letter_prefers_vowels(words, invalids, taken)
            taken.append(c)
            answer = ''
            while len(answer) != no_chars:
                answer = input("MY gUess Is {}. hOW aM i DoINg?".format(c))
            if answer == pattern:
                invalids.append(c)
                tally += 1
            pattern = answer

    if tally >= 12:
        print("I lOse. WAAH!")
    elif len(words) == 1:
        print("YoUr WOrd iS... DRuMroLl... {}!! (i'M aWEsOmE.)".format(words[0]))
    else:
        print("YOu bIG ChEAt. WOrd nOt EXiSt IN my DiCtiONAry!! ")


user_plays()



#computer_plays()









































