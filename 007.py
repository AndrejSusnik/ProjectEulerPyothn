import math


def is_prime(number: int) -> bool:
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


if __name__ == "__main__":
    cnt = 0
    n = 2
    while True:
        if cnt == 10001:
            break

        if is_prime(n):
            cnt += 1

        n += 1


    print(n - 1)
