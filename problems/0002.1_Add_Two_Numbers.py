'''
Runtime: 72 ms, faster than 86.11% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14 MB, less than 65.79% of Python3 online submissions for Add Two Numbers.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        hair = node = ListNode()
        carry = 0
        while l1 or l2 or carry:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            carry, v = divmod(s, 10)
            node.next = ListNode(v)
            node = node.next
        
        return hair.next 
        
        