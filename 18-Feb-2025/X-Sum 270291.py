# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

from collections import defaultdict
t = int(input()) 

for _ in range(t):
    n, m = map(int, input().split())
    chase = [list(map(int, input().split())) for _ in range(n)]
    
    main_diagonal = defaultdict(int)
    cross_diagonal = defaultdict(int)
    
    for i in range(n):
        for j in range(m):
            main_diagonal[i-j] += chase[i][j]
            cross_diagonal[i+j] += chase[i][j]
    
    ans = 0
    
    for i in range(n):
        for j in range(m):
           cur_sum = main_diagonal[i-j] + cross_diagonal[i+j] - chase[i][j]
           ans = max(ans, cur_sum)
    
    print(ans)