# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
n,k = map(int, input().split())
arr = list(map(int, input().split()))


j = 0
counter = 0
max_val = deque()
min_val = deque()

for i in range(len(arr)):
    
    while max_val and arr[max_val[-1]] <= arr[i]:
        max_val.pop()
    max_val.append(i)
    
    while min_val and arr[min_val[-1]] >= arr[i]:
        min_val.pop()
    min_val.append(i)
    
    while arr[max_val[0]] - arr[min_val[0]] > k:
        j += 1
        if max_val[0] < j:
            max_val.popleft()
        if min_val[0] < j:
            min_val.popleft()
            
    counter += i-j +1
           
print(counter)