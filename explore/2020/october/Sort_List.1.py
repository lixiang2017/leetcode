'''
You are here!
Your runtime beats 92.03 % of python submissions.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        array = []
        while head:
            array.append(head.val)
            head = head.next
         
        array.sort()
        
        prev = None
        while array:
            prev = ListNode(array.pop(), prev)
        
        return prev