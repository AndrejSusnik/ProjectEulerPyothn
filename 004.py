if __name__ == "__main__":
    print(max(filter(lambda x: x == int(str(x)[::-1]),
                     [x * y for x in range(100, 1000)
                     for y in range(100, 1000)])))
