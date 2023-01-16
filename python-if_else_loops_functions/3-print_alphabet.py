#!/usr/bin/python3
for i in range(97, 123):
    print(chr(i) + 0 * "{:02}".format(0), end="")
    if i == 101  or i == 113:
        continue
