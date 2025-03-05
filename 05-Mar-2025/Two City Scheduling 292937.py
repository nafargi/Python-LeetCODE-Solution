# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        import math
        # minimum cost if we put x ppl in city a after and including ith ppl
        dp = [[math.inf for _ in range(len(costs) // 2 + 1)] for _ in range(len(costs))]

        for i in range(len(costs) - 1, -1, -1):
            for j in range(min(len(costs) - i + 1, len(costs) // 2 + 1)):
                if i == len(costs) - 1:
                    if j == 0:
                        dp[i][j] = costs[-1][1]
                    else:
                        dp[i][j] = costs[-1][0]
                else:
                    if j == 0:
                        dp[i][j] = costs[i][1] + dp[i + 1][j]
                    else:
                        dp[i][j] = min(costs[i][1] + dp[i + 1][j], costs[i][0] + dp[i + 1][j - 1])
        return dp[0][-1]