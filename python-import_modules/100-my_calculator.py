#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    for i in range(0, len(sys.argv)):
        i += 1

    if i != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    c = sys.argv[2]
    a = sys.argv[1]
    b = sys.argv[3]
    if c not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if c == '+':
        print("{} + {} = {}".format(a, b, add(int(a), int(b))))
    elif c == '-':
        print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
    elif c == '*':
        print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
    else:
        print("{} / {} = {}".format(a, b, div(int(a), int(b))))
