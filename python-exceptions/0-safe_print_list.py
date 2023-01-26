#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    k = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            k += 1
        print()
        return k
    except:
        print()
        return k
