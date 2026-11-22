# abc def
# .- -... -.-.   -.. . ..-.

choice = {
    'a' : '.-',
    'b' : '-...',
    'c' : '-.-.',
    'd' : '-..',
    'e' : '.',
    'f' : '..-.',
}
cowpats = ''
type = input("Welcome to morsecode dictionary! enter your words for us to decode!")
for z in type:
    if z >= 'a' and z <= 'f':
        cowpats = cowpats + choice[z] + ' '
    else:
        cowpats = cowpats + '  '

print(cowpats)
