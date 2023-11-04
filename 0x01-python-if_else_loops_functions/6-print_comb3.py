#!/usr/bin/python3
for j in range(0, 10):
    for k in range(1, 10):
        if j >= k:
            continue
        elif j == 8 and k == 9:
            print("{}{}".format(j, k))
        else:
            print("{}{}".format(j, k), end=", ")
