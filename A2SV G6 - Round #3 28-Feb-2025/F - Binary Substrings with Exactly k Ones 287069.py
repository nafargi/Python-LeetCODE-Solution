# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

from collections import Counter
k = int(input())
s= input().strip()

sum = 0
counter = 0
d = {0:0}

for i in range(len(s)):
   if s[i] == '1':
       sum += 1
   if sum == k:
       counter = counter + 1
   counter += d.get(sum - k,0)
   d[sum] = d.get(sum,0) + 1
print(counter)
