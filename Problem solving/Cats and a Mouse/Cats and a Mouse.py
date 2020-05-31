import math
import os
import random
import re
import sys



if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])

        dist_x = abs(x-z)
        dist_y = abs(y-z)
        if dist_x < dist_y:
            print('Cat B')
        elif dist_x > dist_y:
            print('Cat A')
        else:
            print("Mouse C")

        