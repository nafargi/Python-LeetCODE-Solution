# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans  = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                temp =nums[i] * nums[j]
                ans.append(temp)
            
        result = Counter(ans)
        counter = 0
        for i in result:
            if result[i] > 1:
                pairs= result[i] * (result[i] - 1) // 2
                counter += pairs* 8
        return counter