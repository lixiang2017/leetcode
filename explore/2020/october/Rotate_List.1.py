'''
You are here!
Your runtime beats 94.82 % of python submissions.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # if not head:
        #     return None
        # if not head.next:
        #     return head
        if not head or not head.next:  # union two cases above
            return head
        
        tail = head
        size = 1
        while head.next:  # not head, but head.next
            head = head.next
            size += 1
        
        head.next = tail
        head = head.next
        for i in range(size - k % size - 1):
            head = head.next
            
        current_head = head.next
        head.next = None
        return current_head
        
            
