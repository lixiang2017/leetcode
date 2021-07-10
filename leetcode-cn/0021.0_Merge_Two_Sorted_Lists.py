'''
执行用时：32 ms, 在所有 Python3 提交中击败了98.45% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了37.38%
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = node = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)
                l2 = l2.next
            node = node.next

        node.next = l1 or l2
        return dummy.next
