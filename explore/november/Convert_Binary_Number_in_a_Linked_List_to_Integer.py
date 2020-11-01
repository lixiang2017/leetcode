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
        values = []
        while head:
            values.append(head.val)
            head = head.next
        values = ''.join([str(value) for value in values])
        return int(values, 2)
        