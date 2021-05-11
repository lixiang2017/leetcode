'''
Time: (O(max(M, N)))
Space; O(M + N)

1568 / 1568 test cases passed.
    Status: Accepted
Runtime: 52 ms
Memory Usage: 13.4 MB
    
Submitted: 1 minute ago

You are here!
Your runtime beats 93.90 % of python submissions.
You are here!
Your memory usage beats 73.88 % of python submissions.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        dummy = pre = ListNode()
        carry = 0
        while p1 and p2:
            total = p1.val + p2.val + carry
            if total >= 10:
                total -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(total)
            pre.next = node
            pre = pre.next
            # move to next digit    
            p1 = p1.next
            p2 = p2.next
        
        p = p1 or p2
        while p:
            total = p.val + carry
            if total >= 10:
                total -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(total)
            pre.next = node
            pre = pre.next
            # move to next digit    
            p = p.next
        
        if carry:
            node = ListNode(carry)
            pre.next = node
        
        return dummy.next
            