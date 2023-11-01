#!/usr/bin/python3
for bruno in range(ord('a'), ord('z') + 1):
    if chr(bruno) != 'q' and chr(bruno) != 'e':
        print("{}".format(chr(bruno)), end="")
