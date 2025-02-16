# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

def countSwaps(a):
    temp = 0
    count = 0
    i = 0
   
    while i < len(a):
        idx = 0
        while idx < len(a)-1:
                if a[idx] > a[idx+1]:
                    count = count + 1
                    temp = a[idx]
                    a[idx] = a[idx+1]
                    a[idx+1] = temp
                idx = idx + 1
        i = i + 1
          

    
    print("Array is sorted in " + str(count) + " swaps.") 
    print("First Element:", a[0])