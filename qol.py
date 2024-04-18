from typing import Any, Iterable
from math import sqrt, floor

def intInput(string: Any) -> str:
    return int(input(string))

def isPrime(num: int) -> bool:
    for i in range(2, floor(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def intify(value: Any) -> None:
    value = int(value)

def reverse(value: Iterable) -> None:
    value = value[::-1]