# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        dummy = ListNode(next = head)
        curr = dummy.next

        fast = head
        slow = head

        while fast and fast.next:

            fast = fast.next.next
            slow =  slow.next

            if slow == fast:
                return True
        return False
