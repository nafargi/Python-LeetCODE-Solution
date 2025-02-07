# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

s = "codeforces" 
counter =  0
for _ in range(int(input())):
     x = input()
     for i in range(10):
         if s[i] != x[i]:
             counter += 1
     print(counter)
     counter = 0