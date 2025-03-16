# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))

    max_sum = 0
    curr_max = li[0]  # Start with the first element

    for i in range(1, n):
        if (li[i] > 0) == (curr_max > 0):  # Same sign
            curr_max = max(curr_max, li[i])
        else:  # Sign change
            max_sum += curr_max
            curr_max = li[i]

    max_sum += curr_max  # Add the last segment
    print(max_sum)
