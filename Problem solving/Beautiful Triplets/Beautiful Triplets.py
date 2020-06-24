import math
import os
import random
import re
import sys


def beautifulTriplets(d, arr):
    nums = set(arr)
    return sum(n + d in nums and n + d + d in nums for n in arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
