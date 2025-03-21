# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
            ans = []
            nums =['0','1']
            
            
            def backtrack(temp):
                if len(temp) == n :
                    ans.append("".join(temp))
                    return

                for i in range(2):
                
                    if nums[i] == '0' and len(temp) > 0 and temp[-1] == '0':
                        continue

                    temp.append(nums[i])
                    backtrack(temp)
                    temp.pop()
                
            backtrack([])
            return ans
            
