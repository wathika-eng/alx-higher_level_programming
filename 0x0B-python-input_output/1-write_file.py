#!/usr/bin/python3
"""Write to a file"""

def write_file(filename="", text=""):
    """Write to a file and get number of characters"""
    with open("", mode="w", encoding="utf-8") as f:
        f.write(text)
        return len(text)