# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

n = int (input())

for _ in range(n):
    s = list (input())
    mid = len(s) // 2
    
    if len(s) % 2 != 0:
        print("NO")
    else:
        if s[:mid] == s[mid:]:
            print("YES")
        else:
            print("NO")