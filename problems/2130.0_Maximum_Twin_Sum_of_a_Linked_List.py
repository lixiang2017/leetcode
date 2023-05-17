'''
Runtime: 924 ms, faster than 51.82% of Python3 online submissions for Maximum Twin Sum of a Linked List.
Memory Usage: 47.4 MB, less than 58.59% of Python3 online submissions for Maximum Twin Sum of a Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        half = n // 2
        node1 = node = head
        while half - 1:
            node = node.next
            half -= 1
        # cut
        node2 = node.next
        node.next = None
        
        # insert into head
        prev = None
        while node2:
            nxt = node2.next
            node2.next = prev
            prev = node2
            node2 = nxt
        
        ans = 0
        node2 = prev
        while node1 and node2:
            ans = max(ans, node1.val + node2.val)
            node1 = node1.next
            node2 = node2.next 
        return ans 
        