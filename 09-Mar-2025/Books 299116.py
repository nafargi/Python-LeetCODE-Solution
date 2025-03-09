# Problem: Books - https://codeforces.com/contest/279/problem/B


n, time = map(int, input().split())

book = list(map(int, input().split()))

j = -1
sum_ = 0
ans = 0

for i in range(n):
    if sum_ + book[i] <= time:
        sum_ += book[i]
    else:
        sum_ += book[i]
        while sum_ > time:
            j += 1
            sum_ -= book[j]
    ans = max(ans, i - j)

print(ans)