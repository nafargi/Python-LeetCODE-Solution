# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def oNSpaceSol(s, t):
            s1 = []
            t1 = []

            for char in s:
                if char == "#":
                    if s1:
                        s1.pop()
                else:
                    s1.append(char)

            for char in t:
                if char == "#":
                    if t1:
                        t1.pop()
                else:
                    t1.append(char)
            
            return s1 == t1
        
        def O1SpaceSol(s, t):
            sp = len(s) - 1
            tp = len(t) - 1

            sback = 0
            tback = 0

            while sp >= 0 or tp >= 0:
                print(sp, tp)
                while sp >= 0 and (s[sp] == '#' or sback > 0):
                    if (s[sp] == '#'):
                        sback += 1
                    else:
                        sback -= 1
                    sp -= 1
                
                while tp >= 0 and (t[tp] == '#' or tback > 0):
                    if t[tp] == '#':
                        tback += 1
                    else:
                        tback -= 1
                    tp -=1
                
                if sp >= 0 and tp >= 0 and s[sp] != t[tp]:
                    print('a')
                    return False
                
                if ((sp < 0 and tp >= 0) or (sp >= 0 and tp < 0)):
                    print(sp, tp)
                    print('b')
                    return False
                
                sp -= 1
                tp -= 1
            
            return True
        return O1SpaceSol(s, t)
                        
                            
                

