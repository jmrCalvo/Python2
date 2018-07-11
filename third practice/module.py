#!/usr/bin/python3
import sys,os

if sys.argv[0] is "module.py":
    print(sys.argv[-1])



def problema2():
    x = [i for i in range(0,200) if i % 2 == 0]
    return x[27]

print(problema2())

def factors(n):
    x=[]
    while n>0:
        aux=n % 10;
        n=n//10
        x.append(aux)
    return x

def problema3(n):
    lista=factors(n)
    suma1=0
    suma2=1
    for elem in lista:
        suma1=suma1+elem
    for elem in lista:
        suma2=suma2*elem

    if suma1>suma2:
        return True
    else:
        return False



print(problema3(14))
print(problema3(2))
print(problema3(35))




def problema4(m):
    x=list()
    for index in range(0,m):
        if problema3(index) is False:
            x.append(index)

    return x
print(problema4(8))

def problema5(*mylist):
    x=list()
    for index in range(0,len(mylist)):
        for index2 in range(index+1,len(mylist)):
            if mylist[index] is mylist[index2]:
                if mylist[index]  not in x:
                    x.append(mylist[index])
    return x

print(problema5("hola","hola","adios","chisinau","adios"))

#def recursive(*milista,path,depth,actuallydepth):


#def problema7(path,depth):
    #x=list()
    #for elem in os.listdir(path)
    #        os.pathjoin(path,elem)
    #            x.append(
    #        recursive(x,)
