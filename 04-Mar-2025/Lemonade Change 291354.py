# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                count5 += 1
            elif bills[i] == 10:
                count10 += 1
                if count5 <= 0:
                    return False
                    break
                count5 -= 1

            elif bills[i] == 20:
                if  count5 < 3 and count10 <= 0 :
                    return False
                    break
                elif count5 <= 0 and count10 >0:
                    return False
                    break
               
                if count5 > 2 and count10 <= 0:
                    count5 -= 3
                elif count5 > 0 and count10 > 0:
                    count5 -= 1
                    count10 -= 1
            
        return True