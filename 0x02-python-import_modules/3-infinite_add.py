#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    kount = 0
    for g in range(1, len(argv)):
        kount += int(argv[g])
        print("{}".format(kount))
