# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            tem_arr =arr[i:]
            min_indx_relative = tem_arr.index(min(tem_arr))
            min_indx = i + min_indx_relative
            arr[i],arr[min_indx]  =arr[min_indx],arr[i]
        return arr