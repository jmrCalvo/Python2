#!/usr/bin/python3
import os, sys
import re


def comprobardni(dni):
    if len(dni) is not 9:
        return False
    else:
            letra=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
            numero=int(dni[:-1])
            return letra[numero%23] is dni[-1]

print(comprobardni("77147756Y"))
