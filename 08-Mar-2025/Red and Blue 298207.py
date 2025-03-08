# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = sorted(arr)

    for i in range(1, n):
        arr[i] += arr[i - 1]
        arr2[i] += arr2[i - 1]

    q = int(input())
    for _ in range(q):
        t, l, r = map(int, input().split())
        l -= 1
        r -= 1

        if t == 1:
            if l == 0:
                print(arr[r])
            else:
                print(arr[r] - arr[l - 1])
        else:
            if l == 0:
                print(arr2[r])
            else:
                print(arr2[r] - arr2[l - 1])


if __name__ == "__main__":
    main()
