'''
I do it only in one pass.
T: O(N)
S: O(1)

Runtime: 64 ms, faster than 13.84% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 13.9 MB, less than 87.01% of Python3 online submissions for Reverse Linked List II.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head 
        
        hair = ListNode(next=head)
        node = hair
        for _ in range(left - 1):
            node = node.next 
        
        # node.next  ->  start 
        start = tail = node.next 
        another = None 
        for _ in range(right - left + 1):
            nxt = start.next 
            start.next = another 
            another = start 
            start = nxt 
        
        # link tail to trailing nodes
        tail.next = start
        # link heading-nodes to another
        node.next = another
        
        return hair.next 
        


'''
no need to check left == right

Runtime: 65 ms, faster than 12.39% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 14.2 MB, less than 18.38% of Python3 online submissions for Reverse Linked List II.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        hair = ListNode(next=head)
        node = hair
        for _ in range(left - 1):
            node = node.next 
        
        # node.next  ->  start 
        start = tail = node.next 
        another = None 
        for _ in range(right - left + 1):
            nxt = start.next 
            start.next = another 
            another = start 
            start = nxt 
        
        # link tail to trailing nodes
        tail.next = start
        # link heading-nodes to another
        node.next = another
        
        return hair.next 
        
