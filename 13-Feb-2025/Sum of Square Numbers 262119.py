# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.sqrt(c))

        while a <= b:
            if a * a + b * b == c:
                return True
            elif a * a + b * b > c:
                b -= 1
            else:
                a += 1
        return False