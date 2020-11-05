'''
You are here!
Your runtime beats 23.44 % of python submissions.
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
        if not head:
            return None
        
        dummy = ListNode(-1)
        cur = dummy
        
        while head:
            tmp = head.next   # to keep the next node
            cur = dummy		  # to compare from the beginning
            while cur.next and cur.next.val <= head.val:    # find the suitable position
                cur = cur.next
            head.next = cur.next   # link the dangling node to the left behind
            cur.next = head        # link the dangling node to the former
            head = tmp             # move to the next node
            
        return dummy.next
                    