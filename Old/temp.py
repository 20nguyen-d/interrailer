names = {
    'le': ['le a', 'le b'],
    'nguyen': ['nguyen c', 'nguyen a']
}

print(names)
names['nguyen'].append('nguyen b')

print(len(names))
for surname in names.keys():
    print(surname, ':', names[surname])
print(len(names['le']))

###########
def follow_number_vars():
    numbers = {
        'a': 6,
        'b': 4,
        'c': 2,
    }

    print(numbers.keys())
    a = 'c'
    b = 'a'
    c = 'b'
    numbers[a] = numbers[b] + numbers[c]
    for surname in numbers.keys():
        print(surname, ':', numbers[surname])

    b = a
    a = c
    numbers[a] = numbers[b] + numbers['c'] + numbers[c]
    for surname in numbers.keys():
        print(surname, ':', numbers[surname])
