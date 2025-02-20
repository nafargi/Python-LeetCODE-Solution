# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        dummy = ListNode(next=head)
        temp = dummy
        
        size = 1
        while temp.next:
            size += 1
            temp = temp.next
        
        mid = size // 2
        if size % 2 != 0:
         mid = size // 2 + 1

        
        temp = dummy
        target = 1
        while temp.next:
          if mid == target:
            return temp.next
          temp =temp.next
          target += 1


