# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l= 1
        r = n 
        while l <= r:
           if l == r:
            return l

           mid = (l+r) // 2
           
           if  isBadVersion(mid) :
              r = mid
           else :
              l = mid +1
        return l

           
             
            