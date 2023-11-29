from functools import reduce
from operator import mul
import numpy as np

if __name__ == "__main__":
    numbers: list[list[int]] = []

    with open('011_data.txt') as f:
        lines = f.readlines()
        for line in lines:
            nums = [int(num.strip()) for num in line.split(' ')]
            numbers.append(nums)

    numbers = np.array(numbers)

    print(max([max(reduce(mul, numbers[i: min(i + 4, len(numbers) - 1), j], 1),
                   reduce(mul, numbers[i: max(i - 4, 0), j], 1),
                   reduce(mul, numbers[i, j: min(j + 4, len(numbers[0] - 1))], 1),
                   reduce(mul, numbers[i, j: max(j - 4, 0)], 1),
                   reduce(mul, [numbers[i + n, j + n] for n in range(0, 4) if i + n < len(numbers) and j + n < len(numbers[0])], 1),
                   reduce(mul, [numbers[i + n, j - n] for n in range(0, 4) if i + n < len(numbers) and j - n >= 0], 1))
                for i in range(len(numbers)) for j in range(len(numbers[0]))]))
