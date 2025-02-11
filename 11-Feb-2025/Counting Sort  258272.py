# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    l =[0] * (max(arr)+1)
    for i in range(len(arr)):
        if l[arr[i]] >0:
            l[arr[i]] += 1
        else:
            l[arr[i]] = 1  
    return l