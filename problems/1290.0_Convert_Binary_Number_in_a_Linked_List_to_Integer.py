'''
Runtime: 52 ms, faster than 8.28% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
Memory Usage: 14 MB, less than 89.35% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal, node = 0, head
        while node:
            decimal <<= 1
            decimal |= node.val
            node = node.next
        return decimal
        
        