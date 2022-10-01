'''
two pointers
T: O(1 * N)
S: O(1)

Runtime: 60 ms, faster than 41.68% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.9 MB, less than 70.33% of Python3 online submissions for Remove Nth Node From End of List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        hair = ListNode(next=head)
        first = second = hair 
        i = 0
        while i <= n:
            first = first.next 
            i += 1
        while first:
            first = first.next 
            second = second.next
        second.next = second.next.next
        return hair.next
    