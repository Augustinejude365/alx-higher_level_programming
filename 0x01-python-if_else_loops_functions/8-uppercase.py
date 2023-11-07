#!/usr/bin/python3
def uppercase(str):
    for kase in str:
        if ord("a") <= ord(kase) <= ord("z"):
            kase = chr(ord(kase) - 32)
            print("{:s}".format(kase), end="")
            print()
