# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter
n= int(input())

for _ in range(n):
    s = list(input())
    t = list(input())
    p = list(input())
    
    ds = Counter(s)
    dt = Counter(t)
    dp = Counter(p)
    
    j = 0
    for i in range(len(t)):
        if j < len(s) and s[j] == t[i]:
            j += 1
    
    if j != len(s):
        print("NO")
        continue
            
    ans = True
    for i in dt:
            if ds[i] + dp[i] < dt[i]:
                ans = False
                break
    if ans:
        print("YES")
    else:
       print("NO")


