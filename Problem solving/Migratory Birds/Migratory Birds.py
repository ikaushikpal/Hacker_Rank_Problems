import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.


def migratoryBirds(arr):
    arr_set = list(set(arr))
    maxx = 0
    arr_list = []

    for value in arr_set:
        c = arr.count(value)
        if c > maxx:
            maxx = c

    for value in arr_set:
        c = arr.count(value)
        if c == maxx:
            arr_list.append(value)

    return min(arr_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
