# Problem: Counting Valleys - https://www.hackerrank.com/challenges/counting-valleys/problem

level = 0
valley= 0
input()
for i in input():
    if i == "D":
           level -= 1
    else:
              level += 1
    
    if l == 0 and i == "U": 
          valley+= 1

print(valley)