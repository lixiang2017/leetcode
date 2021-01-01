'''
You are here!
Your runtime beats 81.41 % of python submissions.
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
        if not head:
            return None
        
        nodes = []
        while head and head.val is not None:
            nodes.append(head.val)
            head = head.next
        
        k %= len(nodes)
        nodes = nodes[-k:] + nodes[: -k]
        
        last_node = None
        for node in nodes[::-1]:
            new_node = ListNode(val = node, next = last_node)
            last_node = new_node
        return last_node