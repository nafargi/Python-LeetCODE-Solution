# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import deque

def main():
    n, m = map(int, input().split())

    a = list(map(int, input().split()))

    freq = {}
    q = deque()

    # Variables to track the result
    un = 0  
    res = 0  
    l, r = 0, 0  

    for i in range(n):
        if a[i] not in freq or freq[a[i]] == 0:
            un += 1
        freq[a[i]] = freq.get(a[i], 0) + 1

        q.append(a[i])

        while q and un > m:
            left_element = q.popleft()
            freq[left_element] -= 1
            if freq[left_element] == 0:
                un -= 1

        if res < len(q):
            res = len(q)
            l = i - res + 1
            r = i

    print(l + 1, r + 1)

if __name__ == "__main__":
    main()