#!/usr/bin/python3

gb={
    "|":lambda a, b: a | b,
    "&":lambda a, b: a & b,
    "-":lambda a, b: a - b
}


def funcion(*args):
    x=dict()
    for elem1 in args:
        buleano=False
        for elem2 in args:
            if buleano:
                x.setdefault("%s | %s"%(elem1,elem2),gb["|"](elem1,elem2))
                x.setdefault("%s & %s"%(elem1,elem2),gb["&"](elem1,elem2))
                x.setdefault("%s - %s"%(elem1,elem2),gb["-"](elem1,elem2))
                x.setdefault("%s - %s"%(elem2,elem1),gb["-"](elem2,elem1))
            if elem1 is elem2:
                buleano=True
    return x


print(funcion({1,2,3,4,5},{2,3,4,5,6},{3,4,5,6,7}))

print(funcion({"a","b","c"},{"d","e","f"},{"g","h","j"}))
