import math
import os
import random
import re
import sys


def organizingContainers(container):
    n = len(container)
    row = [0]*n
    col = [0]*n
    for i in range(n):
        for j in range(n):
            row[i] += container[i][j]
            col[i] += container[j][i]

    if sorted(row) == sorted(col):
        print("Possible")
    else:
        print("Impossible")


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        n = int(input())
        container = []
        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        organizingContainers(container)
