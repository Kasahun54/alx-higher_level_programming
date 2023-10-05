#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition"""
    import sys
    argv = len(sys.argv) - 1
    total = 0
    for i in range(argv):
        total += int(argv[i + 1])
    print("{}".format(total))
