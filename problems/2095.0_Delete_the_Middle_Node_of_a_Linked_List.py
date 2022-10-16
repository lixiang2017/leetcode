'''
slow and fast pointers

Runtime: 3834 ms, faster than 41.68% of Python3 online submissions for Delete the Middle Node of a Linked List.
Memory Usage: 60.8 MB, less than 11.84% of Python3 online submissions for Delete the Middle Node of a Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        if slow.next:
            slow.val = slow.next.val
            #
            nextNode = slow.next 
            if nextNode:
                slow.next = nextNode.next
            else:
                slow.next = None
        else:
            head.next = None
        return head
        
