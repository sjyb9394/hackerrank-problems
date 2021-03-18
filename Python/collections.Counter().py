# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
num = int(input())
l = Counter(list(map(int, input().split())))
query = int(input())
ans = 0

for _ in range(query):
    A, B = map(int, input().split())
    if A in l.keys():
        if l[A] > 0:
            ans += B
            l[A] -= 1

print(ans)
    



