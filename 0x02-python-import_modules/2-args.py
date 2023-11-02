#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argJoe = len(sys.argv)
    if argJoe == 1:
        print("{} arguments:".format(argJoe - 1))
    elif argJoe == 2:
        print("{} arguments:".format(argJoe - 1))
    else:
        print("{} arguments:".format(argJoe - 1))
        for b in range(1, argJoe):
            print("{}: {}".format(b, sys.argv[b]))
