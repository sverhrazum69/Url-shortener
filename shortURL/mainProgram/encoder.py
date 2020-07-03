import string
from math import floor

def toBase62(num,b=62):
    base = string.digits + string.ascii_lowercase + string.ascii_uppercase

    index = num % b
    result = base[index]
    tmp = floor(num / b)
    while tmp:
        index = tmp % b
        tmp = floor(tmp/b)
        result += base[index]
    return result
        
