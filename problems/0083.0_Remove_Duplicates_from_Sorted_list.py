'''
Details 
Runtime: 40 ms, faster than 13.53% of Python online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.4 MB, less than 27.24% of Python online submissions for Remove Duplicates from Sorted List.
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
        
        seen = head.val
        last_node = node = head
        while node:
            print 'seen: ', seen, 'node.val: ', node.val
            while node and node.val == seen:
                node = node.next
            if not node:
                break
            last_node.next = node
            last_node = node
            seen = node.val
            node = node.next
        
        last_node.next = None    # dispose the tailing nodes
        
        return head
    