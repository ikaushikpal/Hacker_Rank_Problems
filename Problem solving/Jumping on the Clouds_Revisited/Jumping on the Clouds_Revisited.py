#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))

    e=100
    i=0

    while e!=0:
        i = (i+k)%n
        if i==0:
            break
        if c[i]==1:
            e -= 2
        e -= 1
    if c[0]==1:
        e -= 2
    print(e-1)

    