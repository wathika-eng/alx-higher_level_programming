#!/usr/bin/python3


def uniq_add(my_list=[]):
    rare = set(my_list)
    num = 0
    for i in rare:
        num += i
        return num
