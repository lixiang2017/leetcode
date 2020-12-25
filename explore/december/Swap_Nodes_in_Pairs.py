'''
approach: iterative

You are here!
Your runtime beats 86.64 % of python submissions.

https://leetcode-cn.com/problems/swap-nodes-in-pairs/comments/625099
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # dummy -> pre -> head
        pre = ListNode(None, next = head)
        dummy = ListNode(None, next = pre)
        
        while pre.next and pre.next.next:
            cur = pre.next
            fol = pre.next.next
            # before swap
            #     pre  cur  fol       # previous current follow
            #   　 |    |    |
            # 2 -> 1 -> 3 -> 4 -> 5
            
            
            # after swap
            #          fol  cur
            # 2 -> 1 -> 4 -> 3 -> 5
            cur.next = fol.next
            pre.next = fol
            fol.next = cur
            
            # to next pair
            pre = cur
        
        return dummy.next.next
            
        

