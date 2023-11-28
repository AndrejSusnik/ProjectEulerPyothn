from functools import reduce
import operator

numbers = [int(num) for num in open('./008_data.txt').read() if num != '\n']

print(max([reduce(operator.mul, numbers[i: i + 13], 1)
      for i in range(0, len(numbers) - 12)]))
