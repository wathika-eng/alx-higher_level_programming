#!/usr/bin/python3

import sys

args = len(sys.argv) - 1
if args == 0:
    print("0 arguments.")
elif args == 1:
    print("1 argument:")

else:
    print("{} arguments".format(args))

for a in range(0, args):
    print("{}: {}".format(a + 1, sys.argv[a + 1]))
