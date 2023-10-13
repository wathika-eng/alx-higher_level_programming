#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst_comp = list(a_dictionary.keys())
    lst_comp.sort()
    for aa in lst_comp:
        print("{}: {}".format(a, a_dictionary.get(aa)))
