#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    count = 0
    
    temp_a = 0
    temp_b = 0
    temp_c = 0
    
    
    while temp_b < len(b):
        while temp_a < len(a) and a[temp_a] <= b[temp_b]:
            temp_a += 1
        
        while temp_c < len(c) and c[temp_c] <= b[temp_b]:
            temp_c += 1
        
        count += temp_a * temp_c
        temp_b += 1
    
    return count
    
    
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
