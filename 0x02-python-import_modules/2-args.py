#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    kount = len(sys.srgv) - 1
    if kount == 0:
        print("0 argument.")
    elif kount == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(kount))
        for k in range(kount):
            print("{}: {}".format(k + 1, sys.argv[k + 1]))
