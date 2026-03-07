#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a file named add_item.json.
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# sys.argv[1:] captures all arguments after the script name
items.extend(sys.argv[1:])

save_to_json_file(items, filename)
