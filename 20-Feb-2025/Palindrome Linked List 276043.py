# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        dummy = ListNode(next = head)
        current = dummy.next

        res = []

        while current:
            res.append(current.val)
            current = current.next
        
        return res == res[::-1]
