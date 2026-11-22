family = {
    # 'bo': {
    #     'name': 'Duong',
    #     'age': 40
    # },
    # 'me': {
    #     'name': 'Thao',
    #     'age': 37
    # },
    # 'children': [
    #     {
    #         'name': 'Tun',
    #         'age': 6
    #     },
    #     {
    #         'name': 'Tin',
    #         'age': 3
    #     }
    # ],
    # 'aunt': {
    #     'name': 'Mai',
    #     'age': 40
    # },
}
def read_from_file(filename):
    with open(filename, "r") as fp:
        return fp.read()
# family['aunt'] = {}
# family['aunt']['name'] = 'Mai'
# family['children'] = [{'name': 'Tun', 'age': 6}, {'name': 'Tin', 'age': 3}]


def find_max_age(family):
    max_age = 0
    for x in family['children']:
        if x['age'] > max_age:
            max_age = x['age']
    return max_age
def find_key(x):
    index = x.index(':')
    key = x[:index]
    content = x[index + 1:]
    return key.strip(), content.strip()
# while True:
#     name = input('new name: ')
#     age = int(input('new age:'))
#     for x in family['children']:
#         if x['name'] == name:
#             family['children'].remove(x)
#     if age == -1:
#         break
#     family['children'].append({'name': name, 'age': age})
file = read_from_file("family.txt")
file = file.split("\n")
def make_family(file):
    bo = None
    me = None
    names = []
    ages = []
    for x in file:
        if find_key(x)[0] == 'bo':
            bo = find_key(x)[1]
        if find_key(x)[0] == '  me':
            me = find_key(x)[1]
        if find_key(x)[0] == '    name':
            names.append(find_key(x)[1])
        if find_key(x)[0] == '    age':
            ages.append(find_key(x)[1])
    family['bo'] = {}
    family['bo']['name'] = bo
    family['me'] = {}
    family['me']['name'] = me
    family['children'] = []
    for y in range(len(names)):
        family['children'].append({'name': names[y], 'age': ages[y]})
    return family

big_file = read_from_file("family2.txt")
big_file = big_file.split("\n")

bo = None
me = None
names = []
ages = []
families = []
start = 0
for x in big_file:
    if find_key(x)[0] == 'bo':
        bo = find_key(x)[1]
    if find_key(x)[0] == 'me':
        me = find_key(x)[1]
    if find_key(x)[0] == 'name':
        names.append(find_key(x)[1])
    if find_key(x)[0] == 'age':
        ages.append(find_key(x)[1])
    if x == 'family:':
        family = {}
        family['bo'] = {}
        family['bo']['name'] = bo
        family['me'] = {}
        family['me']['name'] = me
        family['children'] = []
        for y in range(len(names)):
            family['children'].append({'name': names[y], 'age': ages[y]})
        families.append(family)

print(families)





























