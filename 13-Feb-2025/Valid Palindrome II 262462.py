# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        counter = 0
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return s[i:j] == s[i:j][::-1] or s[i+1:j+1] == s[i+1:j+1][::-1]
            
            i += 1
            j -= 1

        return True
