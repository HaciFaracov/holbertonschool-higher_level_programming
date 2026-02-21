#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    
    # Loop x times to check the first x elements
    for i in range(x):
        try:
            # Try to print the item as an integer
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # If the item is a string or list, silently skip it
            pass
            
    # Print an empty line at the very end
    print()
    return count
