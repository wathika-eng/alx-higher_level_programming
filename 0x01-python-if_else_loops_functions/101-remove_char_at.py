#!/usr/bin/python3


def remove_char_at(str, a):
    if a < 0:
        return a
    return str[:a] + str[a + 1 :]
