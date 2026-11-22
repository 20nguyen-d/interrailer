russian_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
nums = '16 12 11 4'
nums = nums.split(' ')
nums = [int(x) for x in nums]
txt = []

for x in nums:
    txt.append(russian_alphabet[x])
finished = 'ЗДРАВСТВУЙТЕ МАРИНА ПОРА ПРИСТУПИТЬ К ПЕРВОМУ ЭТАПУ НАШЕГО ЗАМЫСЛОВАТОГО ПЛАНА'
finished2 = 'ВСТРЕТИМСЯ НА КРАСНОЙ ПЛОЩАДИ КОДОВОЕ СЛОВО:'
finished3 = 'ФЛАГ : ШЕСТНАДЦАТЬ - ДВЕНАДЦАТЬ - ОДИН - ЧЕТЫРНАДЦАТЬДО СКОРОЙ ВСТРЕЧИ АНДРЕЙ'
print(''.join(txt))