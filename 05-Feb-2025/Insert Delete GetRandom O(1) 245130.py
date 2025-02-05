# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.randset=[]

    def insert(self, val: int) -> bool:
        if val not in self.randset:
            self.randset.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.randset:
            self.randset.pop(self.randset.index(val))
            return True
        else:
            return False

    def getRandom(self) -> int:
        import random
        r=random.randint(0,len(self.randset)-1)
        return self.randset[r]