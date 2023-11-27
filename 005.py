import math
from functools import reduce
import operator


def is_prime(number: int) -> bool:
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

def next_prime(number: int) -> int:
    number += 1
    while(not is_prime(number)):
        number += 1
    return number



def lcm(numbers: list[int]) -> int:
    factors: map[int, int] = {n: 0 for n in range(2, max(numbers) + 1) if is_prime(n)}
    for i in numbers:
        f_tmp: map[int, int] = {n: 0 for n in range(2, max(numbers) + 1) if is_prime(n)}
        tmp = i
        divisor = 2
        while tmp != 1:
            while (tmp % divisor == 0):
                tmp /= divisor
                f_tmp[divisor] += 1

            divisor = next_prime(divisor)
        for key, value in f_tmp.items():
            if factors[key] < value:
                factors[key] = value
    return int(reduce(operator.mul, [math.pow(key, value) for key, value in factors.items()], 1))


if __name__ == "__main__":
    print(lcm(range(2, 21)))
