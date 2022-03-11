'''
Runtime: 62 ms, faster than 33.62% of Python3 online submissions for Rotate List.
Memory Usage: 14 MB, less than 54.84% of Python3 online submissions for Rotate List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head 
        
        node = tail = head
        n = 0
        while node:
            n += 1
            tail = node
            node = node.next 
        
        k %= n
        if k == 0:
            return head 
        
        move = n - k - 1
        node = head
        while node.next and move:
            node = node.next
            move -= 1
        
        new_head = node.next
        node.next = None
        tail.next = head 
        return new_head 
    
    