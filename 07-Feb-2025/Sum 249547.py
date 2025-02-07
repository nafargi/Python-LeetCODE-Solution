# Problem: Sum - https://codeforces.com/contest/1742/problem/A

for _ in range(int(input())):
    a, b, c = map(int, input().split(' '))

    if a + b == c:
        print("YES")
    elif a + c == b:
        print("YES")
    elif c + b == a:
        print("YES")
    else:
        print("NO")

