# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)<2:
            return sum(skill)
        f = 0
        l = len(skill)-1
        tot = 0

        skill.sort()
        fix = skill[f] + skill[l]

        while f < l:

            if skill[f] + skill[l] != fix:
                return -1
            tot += skill[f] * skill[l]
            f +=1
            l -=1

        return tot        