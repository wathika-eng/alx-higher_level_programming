#!/usr/bin/python3


def no_c(my_string):
    ccodes = (i for i in my_string if i != "C" and i != "c")
    return "".join(ccodes)
