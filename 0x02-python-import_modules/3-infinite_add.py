#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    sum = 0
    for i in range(n - 1):
        sum += argv[i + 1]
    print("{}".format(sum))
