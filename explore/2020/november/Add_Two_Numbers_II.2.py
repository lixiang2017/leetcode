'''
You are here!
Your runtime beats 84.29 % of python submissions.
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
        def l_to_i(link):
            decimal = 0
            while link:
                decimal = decimal * 10 + link.val
                link = link.next

            return decimal

        decimal_sum = l_to_i(l1) + l_to_i(l2)
        
        def i_to_l(decimal):
            if 0 == decimal:
                return ListNode(0)
            
            pre= None
            while decimal:
                tail = decimal % 10
                pre = ListNode(tail, pre)
                decimal /= 10
            
            return pre
    
        return i_to_l(decimal_sum)
        