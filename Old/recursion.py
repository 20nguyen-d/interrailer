def count_partitions(n, m):
    if n == 0:
        return 1
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def number_sum(n):
    if n == 1:
        return 1
    else:
        return n + number_sum(n - 1)

def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n-2)

def lst_sum(lst):
    total = 0
    for x in lst:
        if isinstance(x, list):
            total += lst_sum(x)
        else:
            total += x
    return total

def convert(s):
    if len(s) == 1:
        return ord(s) - ord('0')
    else:
        return convert(s[:-1]) * 10 + (ord(s[-1]) - ord('0'))

