# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E


t = int(input())  
for _ in range(t):
    input()
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    temp = list(map(int, input().split()))

#i was thouhgt it is simple to do it but i'm cooked bro
    ans = [float('inf')] * n 

    for j in range(k):
        ans[a[j] - 1] = temp[j]  

    for i in range(1, n):
        ans[i] = min(ans[i], ans[i - 1] + 1)

    for i in range(n - 2, -1, -1):
        ans[i] = min(ans[i], ans[i + 1] + 1)

    print(*ans)