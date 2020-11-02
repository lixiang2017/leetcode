'''
You are here!
Your runtime beats 97.61 % of python submissions
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        values.sort()
        pre = None
        while values:
            pre = ListNode(val = values.pop(), next = pre)
        return pre