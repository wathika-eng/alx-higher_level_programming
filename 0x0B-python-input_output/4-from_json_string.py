#!/usr/bin/python3
"""Module that returns an object (Python data structure)"""
import json
def save_to_json_file(my_obj, filename):
    """Function that returns an object (Python data structure)"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)