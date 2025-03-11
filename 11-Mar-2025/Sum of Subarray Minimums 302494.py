# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        next_l = [-1] * n 
        next_r = [n] * n 
        mod = 10**9 + 7
        st = []
        ans = 0

      
        for i in range(n):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if st:
                next_l[i] = st[-1]
            st.append(i)
        print(next_l)

        st.clear()


        for i in range(n-1,-1,-1):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            if st:
                next_r[i] = st[-1]
            st.append(i)
        print(next_r)

        st.clear()

        for i in range(n):
            left_count = i - next_l[i]  
            right_count = next_r[i] - i  
            ans = (ans + arr[i]*left_count*right_count) % mod
        
        return ans



        