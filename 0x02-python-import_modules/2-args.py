# Import the sys module
if __name__ == "__main__":
    import sys

    args = sys.argv
    count = len(args) - 1

    if count == 0:
         print("0 arguments.")
    elif count == 1:
         print("1 argument:")
    elif count > 1:
         print("{} arguments:".format(count))
    for i in range(1, len(args)):
        print(i, ":", args[i])
