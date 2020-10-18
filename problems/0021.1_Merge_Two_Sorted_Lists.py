'''
Success
Details
Runtime: 28 ms, faster than 55.34% of Python online submissions for Merge Two Sorted Lists.
Memory Usage: 13.5 MB, less than 13.68% of Python online submissions for Merge Two Sorted Lists.
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
        array = []
        while l1:
            array.append(l1.val)
            l1 = l1.next
        while l2:
            array.append(l2.val)
            l2 = l2.next
        
        array.sort()
        pre = None
        while array:
            pre = ListNode(array.pop(), pre)
            
        return pre