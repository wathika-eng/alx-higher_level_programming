#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            return(my_list.append(True))
        else:
            return(my_list.append(False))
