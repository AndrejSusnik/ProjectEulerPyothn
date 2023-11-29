from numba import njit, prange
import math


@njit()
def find():
    for a in prange(1, 1000):
        for b in prange(a, 1000):
            for c in prange(b, 1000):
                if a + b + c != 1000 or a ** 2 + b ** 2 != c ** 2:
                    continue
                print(f"Result: {a * b * c}")
                break


if __name__ == "__main__":
    find()
