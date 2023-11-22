import math


def is_prime(number: int):
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def get_lagest_prime_factor(number: int):
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        if not is_prime(i):
            continue

        while (number % i == 0):
            number /= i

        if number == 1:
            return i

    return 1


if __name__ == "__main__":
    print(get_lagest_prime_factor(600851475143))
