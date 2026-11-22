def find_min(number_list):
    min_value = number_list[0]
    for x in number_list:
        if x < min_value:
            min_value = x
    return min_value


def sorting(number_list):
    ordered_list = []
    while len(number_list) > 0:
        actual_min = find_min(number_list)
        ordered_list.append(actual_min)
        number_list.remove(actual_min)
    return ordered_list


def find_index_min(number_list, start):
    min_value_index = start
    for x in range(start, len(number_list)):
        if number_list[x] < number_list[min_value_index]:
            min_value_index = x
    return min_value_index


def proper_sorting(number_list):
    for x in range(len(number_list) - 1):
        min_index = find_index_min(number_list, x)
        print(min_index, x, number_list)
        number_list[min_index], number_list[x] = number_list[x], number_list[min_index]
    return number_list


print(proper_sorting([1, 4, 2, 6, 3]))
