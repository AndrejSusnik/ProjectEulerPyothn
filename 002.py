if __name__ == '__main__':
    vals = [1, 1]
    while vals[-1] + vals[-2] < 4e6:
        vals.append(vals[-1] + vals[-2])
    print(sum(filter(lambda x: x % 2 == 0, vals)))
