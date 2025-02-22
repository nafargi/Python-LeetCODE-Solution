# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)  # Dummy head for the "less than x" list
        greater_head = ListNode(0)  # Dummy head for the "greater or equal to x" list

        less = less_head
        greater = greater_head

        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next

        # Connect the two lists
        less.next = greater_head.next
        greater.next = None

        return less_head.next