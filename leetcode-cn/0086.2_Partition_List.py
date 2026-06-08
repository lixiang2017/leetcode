# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = l = ListNode()
        greater = g = ListNode()
        while head:
            n = head.next
            head.next = None
            if head.val < x:
                l.next = head
                l = l.next
            else:
                g.next = head
                g = g.next
            head = n
        
        l.next = greater.next
        return less.next
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = l = ListNode()
        greater = g = ListNode()
        while head:
            if head.val < x:
                l.next = head
                l = l.next
            else:
                g.next = head
                g = g.next
            head = head.next
        
        g.next = None
        l.next = greater.next
        return less.next
        
