#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    arr.sort()
    left, right = 0, 1
    count = 0
    
    while right < len(arr) and left < len(arr):
        print(arr[right] - arr[left])
        if arr[right] - arr[left] == k:
            count+=1
            right+=1
        else:
            if arr[right] - arr[left] < k:
                right += 1
            else:
                left += 1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
