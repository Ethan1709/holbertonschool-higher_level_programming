#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    k = 0
    r = [val for val in my_list if isinstance(val, (int, float))]
    try:
        for i in range(x):
            print("{:d}".format(r[i]), end="")
            k += 1
        print()
        return k

    except:
        print()
        return k
