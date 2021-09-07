'''
Iteration

You are here!
Your runtime beats 40.01 % of python3 submissions.
You are here!
Your memory usage beats 46.12 % of python3 submissions.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, node = None, head
        while node:
            # back up for next node of the current node
            node_next = node.next
            # change pointers
            node.next = prev
            prev = node
            # to next one
            node = node_next
            
        return prev
