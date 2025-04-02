# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = []
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy.next

        while curr:
            ans.append(curr.val)
            curr= curr.next
        ans.sort()

        sorted_list = ListNode(0)
        curr = sorted_list

        for val in ans:
            curr.next = ListNode(val)
            curr = curr.next

        return sorted_list.next
        

        