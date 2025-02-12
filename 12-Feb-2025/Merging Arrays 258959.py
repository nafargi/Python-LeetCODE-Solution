# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
 
l1 = list(map(int, input().split()))
    
l2 = list(map(int, input().split()))
l3 = []
i = 0
j = 0
size = min(n,m)

while i < n and j < m:
    if l1[i] < l2[j]:
        l3.append(l1[i])
        i += 1
    else:
        l3.append(l2[j])
        j += 1

if i >= n:
 l3.extend(l2[j:])
 
if j >= m:
  l3.extend(l1[i:])
print(*l3)