#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    answer = 0
    flipped_bits = []
    stack = []
    
    for i in range(32):
        if n % 2 == 1:
            stack.append(1)
        else:
            stack.append(0)
        
        n = n//2
    
    for i in range(32):
        bit = stack.pop()
        if bit == 0:
            flipped_bits.append(1)
        else:
            flipped_bits.append(0)
    
    str_temp = ''.join(map(str, flipped_bits))
    return int(str_temp, 2)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
