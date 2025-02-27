# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n =int(input())
s =input()

ans = []
currentIndex = 0
counter = 0

while counter < n:
    if currentIndex < n:
       ans.append(s[currentIndex])
    counter += 1
    currentIndex += counter
   
print("".join(ans))