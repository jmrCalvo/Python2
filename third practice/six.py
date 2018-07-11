#!/usr/bin/python3

gb={
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "-": lambda a, b: a - b
}

def apply_operator(op,a,b):
    f=gb[op]
    return f(a,b)


print(apply_operator("+",2,3))
