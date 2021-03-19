#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    step = [0, 1, 2, 4]
    
    if n < 4: return step[n]

    for i in range(4, n+1):
        step.append(step[i-1]+step[i-2]+step[i-3])
    
    return step[n]
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
