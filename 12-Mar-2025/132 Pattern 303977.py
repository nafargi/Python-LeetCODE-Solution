# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st = []
        ans  = False
        min_val = float('inf')

        for i in range(len(nums)):
           
                min_val = min(nums[i],min_val)

                while st and nums[i] >= st[-1][0]:
                    st.pop()
                if st and nums[i] > st[-1][1]:
                    ans = True
                    break

                st.append((nums[i], min_val))
        return ans
   
       