# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        all_digits ="".join(map(str, nums))
        return [int(all_digits[i]) for i in range(len(all_digits))]