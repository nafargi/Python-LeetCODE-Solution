# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        counter = {0: 1}
        
        for num in nums:
            pre_sum += num
            remainder = pre_sum % k
            counter[remainder] = counter.get(remainder, 0) + 1
        
        ans = 0
        for count in counter.values():
            ans += count * (count - 1) // 2 
        
        return ans
