# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    # Write your code here
    i = 0
    j = 1
    for i in range(n-1):
        t = arr[i+1]
        j = i + 1
        while j > 0:
            
            if arr[j-1] > t:
                arr[j-1], arr[j] = t, arr[j-1]
                
            j -= 1  
        print(*arr)
