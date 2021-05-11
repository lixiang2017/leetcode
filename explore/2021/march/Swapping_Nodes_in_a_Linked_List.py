'''
just swap values, not swap nodes
Time: O(N + N) = O(N)
Space: O(1)

You are here!
Your runtime beats 69.06 % of python submissions.
You are here!
Your memory usage beats 66.43 % of python submissions.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        N = self.linkLength(head)
        # not change
        if N % 2 == 1 and k == (N >> 1) + 1:
            return head
        
        if k > (N >> 1):
            left, right = N + 1 - k, k
        else:
            left, right = k, N + 1 - k

        # just swap left and right values
        l1 = r1 = head
        while left > 1:
            l1 = l1.next
            left -= 1
        while right > 1:
            r1 = r1.next
            right -= 1
        l1.val, r1.val = r1.val, l1.val  
        return head
    
    def linkLength(self, node):
        length = 0
        while node:
            node = node.next
            length += 1
        return length
        