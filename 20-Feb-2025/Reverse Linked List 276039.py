# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        #   dummy = ListNode(next = head)
        #   current = dummy.next
        #   ans = []

        #   while current:
        #     ans.append(current.val)
        #     current = current.next
            
        #   ans = ans[::-1]
        #   dummy = ListNode(next = head)
        #   temp = dummy

        #   for i in range(len(ans)):
        #     temp = temp.next
        #     temp.val = ans[i]
            
        

        #   return dummy.next

        
