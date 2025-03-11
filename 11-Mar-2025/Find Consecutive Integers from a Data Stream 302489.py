# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

#Baraa
class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        self.curr = 0
        

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.curr = 0
            return False
        self.curr = min(self.curr + 1, self.k)
        return self.curr == self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)