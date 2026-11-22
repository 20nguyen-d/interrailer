def get_input(prompt, values):
    c = ''
    while c not in values:
        c = input(prompt)
        if c not in values:
            print('Try again')


    return c

def get_int_input(prompt, min_value, max_value):
    hi = int(input(prompt))
    while hi < min_value or hi > max_value:
        hi = int(input(prompt))
        if hi < min_value or hi > max_value:
            print('try again')


    return hi

# {
#   'r': 'rock',
#   'p': 'paper',
#   's': 'scissor',
# }
def get_dict_input(prompt, dict_values):
    return

value = get_int_input(
    "Enter a value between 1 and 10? ",
    1,
    10
)

print("User input {}".format(value))