'''
Runtime: 63 ms, faster than 29.29% of Python3 online submissions for Partition List.
Memory Usage: 13.8 MB, less than 75.71% of Python3 online submissions for Partition List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = node1 = ListNode()
        greater_equal = node2 = ListNode()
        while head:
            if head.val < x:
                node1.next = head 
                node1 = node1.next 
            else:
                node2.next = head 
                node2 = node2.next 
            head = head.next 
        node1.next = greater_equal.next 
        node2.next = None 
        return less.next 

'''
Runtime: 40 ms, faster than 88.16% of Python3 online submissions for Partition List.
Memory Usage: 16.2 MB, less than 84.23% of Python3 online submissions for Partition List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = node1 = ListNode()
        dummy2 = node2 = ListNode()
        
        while head:
            if head.val < x:
                node1.next = head
                node1 = node1.next 
            else:
                node2.next = head 
                node2 = node2.next
            head = head.next
            
        node2.next = None
        node1.next = dummy2.next
        return dummy1.next
        