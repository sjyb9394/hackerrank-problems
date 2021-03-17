#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    l = []
    d = {'{':'}', '[':']', '(':')'}

    for i in range(len(s)):
        if s[i] == '{' or s[i] == '[' or s[i] == '(':
            l.append(s[i])
        else:
            if not l:
                return "NO"
            
            temp = l.pop()
            if d[temp] != s[i]:
                return "NO"
            
    if not l:
        return "YES"
    
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
