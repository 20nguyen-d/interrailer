my_file = open('input.txt', 'r')
other_file = open('output.txt', 'w')

line = my_file.readline().strip()

lst = []
while line:
    print(line)
    lst.append(line)
    line = my_file.readline().strip()

for x in lst:
    names = x.split(' ', 2)
    firstName = names[0]
    lastName = names[1]
    other_file.write(lastName + ', ' + firstName + '\n')

other_file = open('output.txt', 'r')
line2 = other_file.readline().strip()
while line2:
    print(line2)
    line2 = other_file.readline().strip()

my_file.close()
other_file.close()