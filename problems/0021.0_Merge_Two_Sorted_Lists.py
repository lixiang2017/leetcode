'''
Success
Details
Runtime: 24 ms, faster than 80.09% of Python online submissions for Merge Two Sorted Lists.
Memory Usage: 13.2 MB, less than 13.68% of Python online submissions for Merge Two Sorted Lists.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1, head2 = l1, l2
        dummy = ListNode(-1)
        current = dummy
        
        while head1 and head2:
            if head1.val < head2.val:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next
        
        if not head1:
            current.next = head2
        if not head2:
            current.next = head1
        
        return dummy.next