import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.


def theLoveLetterMystery(s):
    reductions = 0
    for i in range(0, len(s)//2):
        reductions += abs(ord(s[i]) - ord(s[-1-i]))
    return reductions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
