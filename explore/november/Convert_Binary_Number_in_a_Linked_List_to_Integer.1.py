'''
You are here!
Your runtime beats 60.25 % of python submissions.
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
            decimal *= 2
            decimal += head.val
            head = head.next

        return decimal
        