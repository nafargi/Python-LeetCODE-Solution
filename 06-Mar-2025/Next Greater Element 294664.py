# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        dic_next_greater = {}
        ans = [-1] * len(nums1)

        for i in range(len(nums2)):
            while st and st[-1] <= nums2[i]:
                 dic_next_greater[st.pop()] = nums2[i]    
            st.append(nums2[i])

        for i in range(len(nums1)):
            if nums1[i] in  dic_next_greater:
                  ans[i] =  dic_next_greater[nums1[i]]
        return ans