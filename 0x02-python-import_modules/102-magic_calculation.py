#!/usr/bin/python3
from 100-my_calculator.py import add, sub

def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for j in range(4, 6):
            c = add(c, j)
            return (c)
        else:
            return sub(a, b)
