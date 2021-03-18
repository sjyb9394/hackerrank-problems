# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

A = list(map(str, input().split()))

string = list(A[0])
length = int(A[1])

perm = sorted(list(permutations(string, length)))

for p in perm:
    print(''.join(map(str,p)))
