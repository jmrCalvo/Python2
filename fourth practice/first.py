#!/usr/bin/python3
import sys
def funcion(a,b):
    try:
        print(a+b)
    except ArithmeticError:
        print("ArithmeticError")
    except:
        print("Generic exception")
    else:
        print("all ok")
    try:
        print(a-b)
    except ArithmeticError:
            print("ArithmeticError")
    except:
            print("Generic exception")
    else:
            print("all ok")
    try:
        print(a/b)
    except ArithmeticError:
        print("ArithmeticError")
    except:
        print("Generic exception")
    else:
        print("all ok")
    try:
        print(a*b)
    except ArithmeticError:
        print("ArithmeticError")
    except:
        print("Generic exception")
    else:
        print("all ok")


try:
    funcion(int(sys.argv[1]),int(sys.argv[2]))
except:
    print("Invalid parameters")
