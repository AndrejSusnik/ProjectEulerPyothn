import math
from numba import njit, prange

def triangle(number: int) -> int:
    return int(number * (number + 1) / 2)


@njit
def number_of_divisors(number: int) -> int:
    divisors = []
    for i in prange(1, (number // 2) + 1):
        if number % i == 0:
            divisors.append(i)
    return len(divisors) + 1


if __name__ == "__main__":
    num = 2

    while number_of_divisors(triangle(num)) < 500:
        num += 1


