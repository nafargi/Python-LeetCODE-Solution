# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        max_num = float('inf')
        ans = []

        for  j in range(len(list1)):
            if list1[j] in list2:
                for i in range(len(list2)):
                 if list1[j] == list2[i]:
                    if i+j < max_num:   
                        max_num = i+j  
                        ans = [list1[j]]             
                    elif max_num == i+j:
                        ans.append(list1[j])        
        return ans
        