#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argjoe = sys.argv
    sizebee = len(argjoe) - 1
    if sizebee > 1:
        print("{} arguments:".format(sizebee))
        for bat in range(1, sizebee + 1):
            print("{}: {}".format(bat, argjoe[bat]))
        elif sizebee == 0:
            print("{} arguments.".format(sizebee))
        else:
            print("{} argument:".format(sizebee))
            print("{}: {}".format(sizebee, argjoe[1]))
