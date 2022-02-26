'''
merge sort
T: O(NlogN)
S: O(logN)

Runtime: 575 ms, faster than 35.06% of Python3 online submissions for Sort List.
Memory Usage: 30.1 MB, less than 53.90% of Python3 online submissions for Sort List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
    
        # cut
        middle = self.getMid(head)
        md = middle.next
        middle.next = None
        
        a, b = self.sortList(head), self.sortList(md)
        return self.merge(a, b)
    
    
    def getMid(self, node: Optional[ListNode]) -> Optional[ListNode]:
        cur, middle = node, node
        while cur.next and cur.next.next:
            cur, middle = cur.next.next, middle.next     
        return middle
    
    def merge(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode(-1)
        while a and b:
            if a.val < b.val:
                node.next = a
                a = a.next
            else:
                node.next = b
                b = b.next
            node = node.next
        
        if a:
            node.next = a
        if b:
            node.next = b
        
        return dummy.next
    
