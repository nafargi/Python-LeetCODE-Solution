# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if s[0].isalpha():
           s =s.lower()
           first =s[0]

           for i in range(len(s)):
              if s[i] == '@':
                last = s[i-1]
                remain = s[i+1:]

           s = first + '*****' + last + "@"+ remain
           return s

        else:
            nums = []
            for i in range(len(s)):
                if s[i].isdigit():
                    nums.append(s[i])
            nums = "".join(nums)
           
            if len(nums) == 10:
                return "***-***-"+nums[-4:]
            elif len(nums) == 11:
                return "+*-***-***-"+nums[-4:]
            elif len(nums) == 12:
                return "+**-***-***-"+nums[-4:]
            elif len(nums) == 13:
                return "+***-***-***-"+nums[-4:]