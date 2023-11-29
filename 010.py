import math


def is_prime(number: int):
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


print(sum([i for i in range(2, int(2e6)) if is_prime(i)]))
