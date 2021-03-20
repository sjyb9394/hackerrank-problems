# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
A = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))

sym_diff= sorted(A.difference(B).union(B.difference(A)))

for num in sym_diff:
    print(num)
