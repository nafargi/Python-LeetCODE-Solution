# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(next = head)
        temp = dummy
        size = 1
        while temp.next:
            size += 1
            temp = temp.next

        count = size - n
        target =1
        temp = dummy

        while temp.next:
            if target == count:
                temp.next = temp.next.next
            else:
                temp= temp.next
            
            target += 1
        return dummy.next