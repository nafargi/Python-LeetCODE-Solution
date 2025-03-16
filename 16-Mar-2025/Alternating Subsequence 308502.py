# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())


for _ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    
    max_sum = 0
    max_pos= float('-inf')
    max_neg = float('-inf')
    
    for i in range(n):
        if li[i] > 0:
            is_pos = True
        else:
            is_pos = False
            
        if is_pos:
            end_pos = True
            max_pos= max(max_pos,li[i])
            if max_neg != float('-inf') and end_neg:
              end_neg = False
              max_sum += max_neg
              max_neg = float('-inf')
        
        else: 
            end_neg = True
            max_neg= max(max_neg,li[i])
            if max_pos != float('-inf') and end_pos:
              max_sum += max_pos
              end_pos = False
              max_pos = float('-inf')
              
    if max_pos != float('-inf'):
        max_sum += max_pos
    if max_neg != float('-inf'):
        max_sum += max_neg
        
    print(max_sum)
            
    
    
