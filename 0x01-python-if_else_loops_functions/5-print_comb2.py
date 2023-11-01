#!/usr/bin/python3
for joe in range(0, 100):
    if joe == 99:
        print("{}".format(joe))
    else:
        print("{:02}".format(joe), end=", ")
