# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
            ans = [[]] * 2
            player_wins = set()
            loss_freq = Counter()
        
            for i in matches:
                winner = i[0]
                loser = i[1]

                player_wins.add(winner)
                loss_freq[loser] += 1
                
            all_winners = []
            for i in player_wins:
                if i not in loss_freq:
                    all_winners.append(i)
        
            ans[0] = sorted(all_winners)
            
            all_loser = []
       
            for i ,counter in loss_freq.items():
                if counter == 1:
                    all_loser.append(i)
                

            ans[1] = sorted(all_loser)

            return ans