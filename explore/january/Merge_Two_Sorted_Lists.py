'''
Time: O(M + N), M is the length of l1 and N is the length of l2
Space: O(1)

You are here!
Your runtime beats 44.77 % of python submissions.
You are here!
Your memory usage beats 99.87 % of python submissions.
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
        dummy = node = ListNode(0)
        node1 = l1
        node2 = l2

        while node1 and node2:
            if node1.val <= node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next
        
        if node1:
            node.next = node1
        else:
            node.next = node2
        
        return dummy.next
        
        