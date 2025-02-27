# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

t = int(input())

for _ in range(t):
        a = list(input().split())
        n = a[0]
        m = a[1]
        d = {'L':2, "M":1 ,"S":0}
        
        
        for i in d:
            if n[len(a[0]) - 1] == i:
                left = d[i]
            if m[len(a[1]) - 1] == i:
                right= d[i]
        if left > right:
                print(">")
        elif left < right:
                print("<")
        elif left == right:
                if len(n) == len(m):
                        print("=")
                elif len(n) != len(m) and n[len(a[0]) - 1] == 'S':
                        if len(n) < len(m):
                            print(">")
                        else:
                           print("<")
                elif len(n) != len(m):
                        if len(n) > len(m):
                            print(">")
                        else:
                            print("<")