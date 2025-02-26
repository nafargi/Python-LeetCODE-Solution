# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

n = int(input())

for _ in range(n):
    a=int(input())
    b=list(input().strip())
    c=list(input().strip())
    
    z= 0 #zero counter
    o = 0 #one counter
    v = True
    idx = -1
    ans = True 
    
    for j in range(len(b)):
        if b[j] == '0':
            z += 1
        else:
            o += 1
            
        if z == o:
            isSame = b[j] == c[j]
            k = j
            
             # the critical point is here my nigga...
            while k > idx:
                if isSame and b[k] != c[k]:
                    ans = False
                    break
                elif not isSame and b[k] == c[k]:
                    ans = False
                    break
                k -= 1
            if not  ans:
                break
            idx = j
            z = 0
            o= 0
    for j in range(len(b)-1, idx,-1):
        if b[j] != c[j]:
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")
        
 
        
        
