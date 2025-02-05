# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0] * len(indices)

        for i in range(len(indices)):
            ans[indices[i]] = s[i]
        return "".join(ans)