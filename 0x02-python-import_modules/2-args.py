#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argJoe = len(sys.argv)
    if argJoe == 1:
        print("{} arguments.".format(argJoe - 1))
    elif argJoe == 2:
        print("{} argument:".format(argJoe - 1))
    else:
        print("{} arguments:".format(argJoe - 1))
        for bat in range(1, argJoe):
            print("{}: {}".format(bat, sys.argv[bat]))
