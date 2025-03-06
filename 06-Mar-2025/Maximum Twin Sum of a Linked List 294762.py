# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: ListNode) -> int:
        values = []
        temp = head

        while temp:
            values.append(temp.val)
            temp = temp.next

        max_sum = float('-inf')
        n = len(values)

    
        for i in range(n // 2):
            max_sum = max(max_sum, values[i] + values[n - 1 - i])

        return max_sum