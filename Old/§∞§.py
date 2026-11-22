import copy
number = int(input("Give me a NUMBER! "))
def numbers(number):
    all_numbers = []
    while number > 0:
        new_number = number % 10
        all_numbers.append(new_number)
        number = number // 10
    return all_numbers
nums = numbers(number)



def max_list(nums):
    max = nums[0] if len(nums) > 0 else -1
    index = 0
    for x in range(len(nums)):
        if nums[x] < max:
            max = nums[x]
            index = nums.index(max)
    return max, index


def sort_list_asc(nums):
    final_nums = []

    while len(nums) > 0:
        maxv, index = max_list(nums)
        del nums[index]
        final_nums.append(maxv)

    return final_nums



def min_list(nums):
    min = nums[0] if len(nums) > 0 else -1
    index = 0
    for x in range(len(nums)):
        if nums[x] > min:
            min = nums[x]
            index = nums.index(min)
    return min, index

def sort_list_des(nums):
    final_nums = []

    while len(nums) > 0:
        minv, index = min_list(nums)
        del nums[index]
        final_nums.append(minv)

    return final_nums

def make_A_number(nums):
    number = len(nums)
    for x in range(len(nums)):
        number = number - 1
        nums[x] = nums[x] * (10**number)
    return nums

def formula(nums):
    dsc = (sort_list_asc(copy.copy(nums)))
    asc = (sort_list_des(copy.copy(nums)))
    asc_num = (sum((make_A_number(asc))))
    dsc_num = (sum((make_A_number(dsc))))
    stop = False
    previous = -1
    while not stop:
        new_num = asc_num - dsc_num
        print(new_num)
        dsc = (sort_list_asc(copy.copy(numbers(new_num))))
        asc = (sort_list_des(copy.copy(numbers(new_num))))
        asc_num = (sum((make_A_number(asc))))
        dsc_num = (sum((make_A_number(dsc))))

        if new_num == previous:
            stop = True

        previous = new_num


    return previous
print(formula(copy.copy(nums)))








































































