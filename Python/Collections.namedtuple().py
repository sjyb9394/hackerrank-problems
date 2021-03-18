# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

A = int(input())
table = namedtuple('table', input())
answer = 0

for _ in range(A):
    t = table(*input().split())
    answer += int(t.MARKS)
    
print('{:.2f}'.format(answer/A))

