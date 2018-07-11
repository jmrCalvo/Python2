#!/usr/bin/python3

gb={
    "print_all": lambda *a, **k: print(a, k),
    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
    "print_only_args": lambda *a, **k: print(a),
    "print_only_kwargs": lambda *a, **k: print(k)
}



def apply_operator(op,a,b):
    f=gb[op]
    if f==False:
        gb[op]=lambda a, b: a op b
        f=gb[op]
    return f(a,b)


print(apply_operator("+",2,3))
