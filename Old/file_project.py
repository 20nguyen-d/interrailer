def read_from_file(filename):
    with open(filename, "r") as fp:
        return fp.read()
def write_to_file(filename, content):
    with open(filename, "a") as fp:
        fp.write("\n" + content)
my_list = read_from_file('input.txt').split('\n')
a = {'bo': 'duong', 'me': 'thao', 'children': {'tun': 12, 'vy': 7, 'tin': 0}}
name = None
a['children']['ton'] = 16
max_age = max(a['children'].values())
print(max_age)
for y in a['children'].keys():
    if a['children'][y] == max_age:
        name = y

print(max_age, name)