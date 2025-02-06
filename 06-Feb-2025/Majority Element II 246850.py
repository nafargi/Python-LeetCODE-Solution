# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict_freq = Counter(nums)
        ans = []

        for i in dict_freq:
           if  dict_freq[i] > len(nums)/3:
             ans.append(i)
             
        return ans