# Enter your code here. Read input from STDIN. Print output to STDOUT

l = list(map(int, input()))
temp = l[0]
count = 1
ans = []

if len(l)==1:
    print((count,temp))

for i in range(1, len(l)):
    if l[i] == temp:
        count+=1
    else:
       ans.append((count,temp))
       temp = l[i]
       count = 1
       
    if i == len(l)-1:
        ans.append((count,l[i])) 

for p in ans:
    print(p, end=" ")
