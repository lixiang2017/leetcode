'''
Runtime: 60 ms, faster than 95.01% of Python3 online submissions for Insertion Sort List.
Memory Usage: 17.4 MB, less than 7.76% of Python3 online submissions for Insertion Sort List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        values.sort()
        pre = None
        while values:
            pre = ListNode(val=values.pop(), next=pre)
        return pre   
        