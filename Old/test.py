import hashlib
def read_from_file(filename):
  with open(filename, "r") as fp:
    return fp.read()
sequence = read_from_file("blackflag.txt")

def pid_finder(protein, number):
  pid = []
  pid.append(number)
  for x in range(16):
    pid.append(protein[number-1])
    number = number + 100
  return ''.join([str(x) for x in pid])

binary = '01110011 01101111 01101100 01110110 01100101 00100000 01110100 01101000 01100101 00100000 01110000 01110101 01111010 01111010 01101100 01100101 01110011'.split(' ')
def binary_to_letter(sequence):
  numbers = []
  letters = []
  for x in sequence:
    numbers.append(int(x, 2))
  for y in numbers:
    letters.append(chr(y))
  return(''.join(str(z) for z in letters))


def fibonacci(n):
  number1 = 1
  number2 = 1
  fibonacci = [1, 1]
  for x in range(n):
    fibonacci.append(number2+number1)
    number1, number2 = number2, number1 + number2

  return fibonacci[n-1]


str_alphabet = "abcdefghijklmnopqrstuvwxyz"
list_alphabet = [x for x in str_alphabet]

def caesar_decode(text, key, alphabet):
  plain_text = ""
  for letter in text:
    if letter in alphabet:
      i = alphabet.find(letter)
      j = i - key
      plain_text = plain_text + alphabet[j % 26]
    else:
      plain_text = plain_text + letter
  return plain_text

def remove_duplicates(text):
  no_duplicates = []
  for x in text:
    if x not in no_duplicates:
      no_duplicates.append(x)
  return ''.join(str(x) for x in no_duplicates)

def get_new_alphabet(text, key):
  no_duplicate_string = remove_duplicates(text)
  second_string = []
  for x in list_alphabet:
    if x not in no_duplicate_string:
      second_string.append(x)
  new_alphabet = no_duplicate_string + ''.join(str(x) for x in second_string)
  a = new_alphabet+new_alphabet
  shifted_alphabet = a[key:52-key]
  return shifted_alphabet[:26]
encrypted = read_from_file("caesar_cipher_to_decode.txt")

def super_cracker(text):
  new_alphabet = (get_new_alphabet('dalmatians', 3))
  normal_alphabet = 'abcdefghijklmnopqrstuvwxyz'
  decoded = []
  for x in text.lower():
    if x in new_alphabet:
      my_index = new_alphabet.index(x)
      decoded.append(normal_alphabet[my_index])
    else:
      decoded.append(x)
  return ''.join([str(y) for y in decoded])

def md5_encode(word):
  binary_word = word.encode("UTF-8")
  encrypted_password = hashlib.md5(binary_word).hexdigest()
  return encrypted_password


def super_encoder(text, keyword, number):
  new_alphabet = get_new_alphabet(keyword, number)
  normal_alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encoded = []
  for x in text:
    if x in normal_alphabet:
      my_index = normal_alphabet.index(x)
      encoded.append(new_alphabet[my_index])
    else:
      encoded.append(x)
  return (''.join([str(y) for y in encoded])).upper()


previous = [0]
next = [1]
for x in range(len(previous) - 1):
  next.append(previous[x] + previous[x + 1])
next.append(1)
print(next)


class Solution(object):
  def searchInsert(self, nums, target):
    '''
    [1,3,5,6]
5
    '''
    min_index = 0
    max_index = len(nums) - 1
    mid_index = max_index // 2
    if target < nums[min_index] or target > nums[max_index]:
      return max_index + 1
    while max_index - min_index != 1:
      if target < nums[max_index] and target > nums[mid_index]:
        min_index = mid_index
        mid_index = (max_index + min_index) // 2
      if target > nums[min_index] and target < nums[mid_index]:
        max_index = mid_index
        mid_index = (max_index + min_index) // 2
      if target == nums[min_index]:
        return min_index
      if target == nums[mid_index]:
        return mid_index
      if target == nums[max_index]:
        return max_index

































































