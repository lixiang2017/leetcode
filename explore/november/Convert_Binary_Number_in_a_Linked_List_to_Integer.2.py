'''
O(n) time with O(1) space
use bits operation

You are here!
Your runtime beats 84.72 % of python submissions.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        decimal = 0
        while head:
            # decimal *= 2   # same as decimal <<= 1
            decimal <<= 1
            # decimal += head.val   # same as decimal |= head.val
            decimal |= head.val   
            head = head.next

        return decimal
        