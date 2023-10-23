#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    tt = 0
    for a in range(x):
        try:
            print(f"{my_list[a]}", end="")
            tt += 1
        except Exception:
            break
    print()
    return tt
