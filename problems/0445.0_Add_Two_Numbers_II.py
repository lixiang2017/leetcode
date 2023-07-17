'''
stack + stack

Runtime: 79 ms, faster than 76.22% of Python3 online submissions for Add Two Numbers II.
Memory Usage: 16.4 MB, less than 68.70% of Python3 online submissions for Add Two Numbers II.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        another, carry = None, 0
        while stack1 or stack2 or carry:
            s = (stack1.pop() if stack1 else 0) + (stack2.pop() if stack2 else 0) + carry
            carry, x = divmod(s, 10)
            another = ListNode(x, another)
        return another
