#!/usr/bin/python3

import sys
import operator

NUM_ARGS = 4;

funciones = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '%': operator.truediv
             }

if __name__ == "__main__":

    if len(sys.argv) != NUM_ARGS:
        sys.exit('Usage error: <num1> <operator> <num2>')

    try:
        sol = funciones[sys.argv[2]]
        print(sol(float(sys.argv[1]), float(sys.argv[3])))
    except (KeyError, ValueError):
        sys.exit('Invalid operation')
    except ZeroDivisionError:
        sys.exit('Error: divided by zero')
