#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    arez = [(x * y) for x, y in my_list]
    othmane = [(y) for x, y in my_list]
    total_arez = 0
    for i in range(len(arez)):
        total_arez = total_arez + arez[i]
    total_othmane = 0
    for j in range(len(othmane)):
        total_othmane = total_othmane + othmane[j]
    return(total_arez / total_othmane)
