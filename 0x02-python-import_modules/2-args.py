#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    kountag = len(sys.argv) - 1
    if kountag == 0:
        print("0 arguments.")
    elif kountag == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(kountag))
        for bat in range(kountag):
            print("{}: {}".format(bat + 1, sys.argv[bat + 1]))
