#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    # Start from index 1 to skip the script name itself
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])

    print("{}".format(total))
