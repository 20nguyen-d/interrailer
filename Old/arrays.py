question =  input(' Give me a sentence to decode or encode ')
result = ''
for c in question:
    if c >= 'a' and c <= 'z':
        answer = ord(c) + 13
        if answer > 122:
            answer = answer - 26
    elif c >= 'A' and c <= 'Z':
        answer = ord(c) + 13
        if answer > 90:
            answer = answer - 26
    else:
        answer = ord(c)

    result = result + chr(answer)

print('original is {} your code is {} '.format(question, result))