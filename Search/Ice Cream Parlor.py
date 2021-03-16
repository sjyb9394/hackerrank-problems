#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    d = {}
    
    for i, num in enumerate(cost):
        n = money - num
        if n not in d:
            d[num] = i+1
        else:
            print(d[n],i+1)
            break 
        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
