def write_to_file(filename, content):
    with open(filename, "a") as fp:
        fp.write("\n" + content)


def read_from_file(filename):
    with open(filename, "r") as fp:
        return fp.read()

def sort_file():
    new_item = input('Enter your item here: ')
    content = read_from_file("tun.txt").split("\n")
    while new_item != 'stop':
        if new_item in content or new_item == '':
            new_item = input('Enter your item here(try another): ')
        else:
            content.append(new_item)
            new_item = input('Enter your item here: ')
    sorted_items = sorted(content)
    all_new_items = '\n'.join(sorted_items)
    write_to_file("tun.txt", all_new_items)
    print(sorted_items)

numbers = read_from_file("input.txt").split("\n")
numbers = [int(x) for x in numbers]
sum_of_numbers = sum(numbers)
print(sum_of_numbers)
mean = sum_of_numbers/len(numbers)
print(mean)
sorted_numbers = sorted(numbers)
median = sorted_numbers[len(numbers)//2]
print(median)
outputs = [sum_of_numbers, mean, median]
outputs = [str(x) for x in outputs]
ready_outputs = '\n'.join(outputs)
write_to_file("output.txt", ready_outputs)