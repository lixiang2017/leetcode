'''
Success
Details 
Runtime: 36 ms, faster than 31.50% of Python online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.7 MB, less than 27.24% of Python online submissions for Remove Duplicates from Sorted List.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        values = [head.val]
        while head:
            if values[-1] != head.val:
                values.append(head.val)
            head = head.next
        
        # to form a new singly-linked list
        pre_node = None
        while values:
            pre_node = ListNode(values.pop(), pre_node)
        
        return pre_node
    