# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

from itertools import accumulate

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        m = int(input())
        b = list(map(int, input().split()))

        a_prefix = list(accumulate(a))
        b_prefix = list(accumulate(b))

        max_a = max(a_prefix, default=0)
        max_b = max(b_prefix, default=0)

        print(max(0, max_a) + max(0, max_b))


if __name__ == "__main__":
    main()
