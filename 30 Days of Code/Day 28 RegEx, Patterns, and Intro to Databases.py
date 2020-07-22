import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    id = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if '@gmail' in emailID:
            id.append(firstName)
    
    id.sort()
    for i in id:
        print(i)
    