# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       
        dummy = ListNode(0, head)
        prev_group_tail = dummy

        curr = head
        while True:
            count = 0
            temp = curr
            while temp and count < k:
                temp = temp.next
                count += 1
            if count < k:
                break

            prev = None
            curr_group_head = curr
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            curr_group_head.next = curr
            prev_group_tail.next = prev 
            prev_group_tail = curr_group_head 
        return dummy.next
