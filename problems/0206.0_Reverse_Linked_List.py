'''
iteratively

Runtime: 60 ms, faster than 40.75% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.4 MB, less than 93.96% of Python3 online submissions for Reverse Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        another = None 
        while head:
            nxt = head.next 
            head.next = another 
            another = head 
            head = nxt 
        return another 
    
'''
recursively

// original list
head -> head.next -> ... -> node
// node = self.reverseList(head.next)
node -> ... -> head.next -> None
// return node
node -> ... -> head.next -> head -> None


Runtime: 55 ms, faster than 52.68% of Python3 online submissions for Reverse Linked List.
Memory Usage: 20.5 MB, less than 9.01% of Python3 online submissions for Reverse Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        node = self.reverseList(head.next)
        head.next.next = head 
        head.next = None 
        return node  
    
