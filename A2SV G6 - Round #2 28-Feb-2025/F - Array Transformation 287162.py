# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter

for i in range(int(input())):
    n = int(input())
    a= list(map(int,input().split()))
    j =0
    
    freq = Counter(a)
    freq_list = list(freq.values())
    min_val = float('inf')
    size = len(a)
    
    for counter in set(freq_list):
        remove = 0
        for k in freq:
            if counter <= freq[k]: 
                remove += counter
        min_val = min(size - remove,min_val)
    print(min_val)
            
