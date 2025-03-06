# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        st = []
        for i in range(len(temperatures)):
          while st and st[-1][0] < temperatures[i]:
             val = st.pop()
             ans[val[1]] =  i - val[1]
          st.append((temperatures[i],i))
        return ans
