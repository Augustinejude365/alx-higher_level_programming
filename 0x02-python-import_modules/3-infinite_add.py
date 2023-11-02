#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    outcome = 0
    for k in sys.argv:
        if k.isdigit():
            outcome += int(k)
        else:
            print("Error: Invalid input. Please enter a valid integer.")
            print("{}".format(outcome))
