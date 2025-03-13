# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbit_freq = Counter(answers)
        counter = 0

        for r in rabbit_freq:
            if r == 0:
                counter += rabbit_freq[r]
            elif r +1 >= rabbit_freq[r]:
                counter += r + 1
            else:
                it =  rabbit_freq[r]
                while it > 0:
                    it -= r + 1
                    counter += r +1
                
       
        return counter
