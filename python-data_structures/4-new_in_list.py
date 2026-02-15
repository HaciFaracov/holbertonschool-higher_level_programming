#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Always create a copy first
    copy = my_list[:]
    # Check boundaries
    if idx < 0 or idx >= len(my_list):
        return copy
    # Modify the copy, not the original
    copy[idx] = element
    return copy
