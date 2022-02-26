'''
DFS

Runtime: 42 ms, faster than 50.40% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.8 MB, less than 99.33% of Python3 online submissions for Swap Nodes in Pairs.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 

        other = head.next.next
        other_h = self.swapPairs(other)
        head.next.next = None
        second = head.next
        second.next, head.next = head, other_h
        return second
        
        
'''
Runtime: 28 ms, faster than 93.46% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.9 MB, less than 90.54% of Python3 online submissions for Swap Nodes in Pairs.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 

        other_h = self.swapPairs(head.next.next)
        head.next.next = None
        second = head.next
        second.next, head.next = head, other_h
        return second
        
        
        