def intInput(string: str) -> str:
    return int(input(string))

def isPrime(num: int) -> bool:
    from math import sqrt
    if num < 2: # if num isn't "prime-or-not"able
        return None
    for i in range(sqrt(num), 1, -1):
        if num % i == 0:
            return False
    return True

def retype(value, type):
    return type(value)