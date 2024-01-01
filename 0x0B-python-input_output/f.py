# /usr/bin/python3

import os

with open("me.txt", mode="w", encoding="utf-8") as f:
    f.write("Hello, World!\n")

with open("me.txt", mode="r", encoding="utf-8") as f:
    print(f.readline())
