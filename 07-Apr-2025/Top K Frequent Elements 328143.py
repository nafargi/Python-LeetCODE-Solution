# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_frq = Counter(nums)
        max_frq = max(dict_frq.values()) if dict_frq else 0
        bucket_li = []

        for _ in range(max_frq+1):
            bucket_li.append([])

        for key,val in dict_frq.items():
             bucket_li[val].append(key)

        ans =[]
        count =0

        for i in range(len(bucket_li)-1,-1,-1):
            
            if bucket_li[i]: 
                for num in bucket_li[i]:
                    if count < k:
                        ans.append(num)
                        count += 1
                    else:
                        break
                if count >= k:
                    break

        
        return ans

     

    




        
    
        