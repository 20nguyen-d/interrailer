string1 = 'hello'
string2 = 'hellohellohh'
tally = 0
output = []
def find_extra_str(string1, string2):
    tally = 0

    output = []
    for x in range(len(string2)):
        if tally == len(string1):
            output.append(string2[x:])
            break
        elif string2[x] == string1[tally]:
            tally = tally + 1
        else:
            output.append(string2[x])

    return output
print(find_extra_str("abc", "12abc"))
print(find_extra_str("abc", "abc45"))
print(find_extra_str("abc", "ababcababc"))