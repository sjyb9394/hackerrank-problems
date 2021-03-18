# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A, B = map(int, input().split())
num = []

for _ in range(A):
    num.append(list(map(int, input().split()))[1:])   

total_num = list(map(lambda x: sum(i**2 for i in x)%B, product(*num)))

print(max(total_num))
