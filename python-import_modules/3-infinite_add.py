#!/usr/bin/python3
import sys

if __name__ == "__main__":
    summ = sum(int(i) for i in sys.argv[1:])
    print(summ)
