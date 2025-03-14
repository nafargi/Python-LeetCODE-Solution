# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    counter = 0
    max_val =0
    
    for i in range(n):
      if max_val > arr[i]:
          max_val = 0
          counter += 1
      else:
          max_val = arr[i]
          
    print(counter)
          