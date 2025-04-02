# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        low = 0
        high = len(citations) -1
        n = len(citations)

        if citations[-1] == 0:
           return 0 

        while low <= high:
            mid = (low + high) //2 

            if citations[mid] < n-mid:
                low = mid +1
            else:
                high = mid -1
        
        return n - low
        
        


        