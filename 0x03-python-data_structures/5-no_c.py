#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for my_elements in my_string:
        if my_elements != "c" and my_elements != "C":
            new_string += my_elements
            return new_string
