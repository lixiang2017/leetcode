'''
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 43.43 % of python submissions.
You are here!
Your memory usage beats 88.28 % of python submissions.
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
        dummy = node = ListNode(0)
        while head:
            start = head
            jump = start.next
            isDuplicate = False
            while jump and start.val == jump.val:
                jump = jump.next
                isDuplicate = True
            
            if not isDuplicate:
                node.next = start
                node = node.next
                head = jump
            else:
                node.next = None  # [1,2,2]
                head = jump
            
        return dummy.next
    