# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
          
        curr = head
        seen = set()
        ans = []
       

        while curr:
            if curr.val not in seen:
               seen.add(curr.val)
               ans.append(curr.val)
            curr = curr.next
        
        ans.sort()
        dummy = ListNode(0)
        res = dummy
        
        for i in ans:
            res.next = ListNode(i)
            res = res.next
        
        return dummy.next