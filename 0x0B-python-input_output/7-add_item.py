#!/usr/bin/python3
"""Adding Items"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').
    load_from_json_file

    args = sys.argv
    filename = "add_item.json"
    with open(filename, 'a+', encoding="utf-8") as f:
        items = []
        my_list.append(args[1:])
        save_to_json_file(items, filename)
        load_from_json_file(filename)
