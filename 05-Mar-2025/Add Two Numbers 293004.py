# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.getnum(l1)
        num2 = self.getnum(l2)
        result = str(num1 + num2)[::-1]
        x = ListNode(int(result[0]))
        temp = x
        for i in result[1:]:
            temp.next = ListNode(int(i))
            temp = temp.next
        return x
    
    def getnum(self, l):
        num = ""
        head = l
        while head:
            num += str(head.val)
            head = head.next
        return int(num[::-1])