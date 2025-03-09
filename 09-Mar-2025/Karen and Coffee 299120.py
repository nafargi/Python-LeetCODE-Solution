# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

N = 200005

n, k, q = map(int, input().split())

f = [0] * N

for _ in range(n):
    l, r = map(int, input().split())
    f[l] += 1
    if r + 1 < N:
        f[r + 1] -= 1

cnt = 0
for i in range(N):
    cnt += f[i]
    f[i] = 1 if cnt >= k else 0

p = [0] * N
for i in range(1, N):
    p[i] = f[i - 1] + p[i - 1]

for _ in range(q):
    l, r = map(int, input().split())
    print(p[r + 1] - p[l])