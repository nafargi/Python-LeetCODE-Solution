# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

from collections import Counter
t = int(input())
points = []
for _ in range(t):
    i , j = map(int,input().split())
    points.append([i,j])

point2 = []
for i in range(len(points)):
    point2.append([points[i][0],1])
    point2.append([points[i][1]+1,-1])

point2.sort()

dic = {}
prev = None
actv = 0

for i in range(len(point2)):
    curr = point2[i][0]
    if prev is not None and curr != prev:
        
        point = curr - prev 
        if point > 0 :
            dic[actv] = dic.get(actv, 0) + point
    actv += point2[i][1]
    prev = curr

ans = []
for i in range(1,t+1):
        ans.append(str(dic.get(i, 0)))
print(*ans)