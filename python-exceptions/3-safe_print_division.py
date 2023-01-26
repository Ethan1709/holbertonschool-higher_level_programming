#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a / b
    except:
        return
    finally:
        if b == 0:
            print("Inside result: " + str(None))
        else:
            print("Inside result: " + str(a / b))
