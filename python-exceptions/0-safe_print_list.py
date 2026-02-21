#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        # Try to loop x times
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    
    # Print an empty line at the very end
    print()
    return count
