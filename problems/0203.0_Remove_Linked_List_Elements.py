'''
T: O(N)
S: O(1)

Runtime: 68 ms, faster than 78.34% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 17.1 MB, less than 68.19% of Python3 online submissions for Remove Linked List Elements.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = prev = ListNode(next = head)
        cur = prev.next
        while cur:
            if cur.val != val:
                prev.next = cur
                prev = prev.next
                cur = cur.next
            else:  
                cur = cur.next
        prev.next = None
        
        return dummy.next


'''
T: O(N)
S: O(1)

Runtime: 72 ms, faster than 58.90% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 17.1 MB, less than 90.75% of Python3 online submissions for Remove Linked List Elements.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = prev = ListNode(next = head)
        cur = prev.next
        while cur:
            if cur.val != val:
                prev.next = cur
                prev = prev.next 
            cur = cur.next
        prev.next = None
        
        return dummy.next

