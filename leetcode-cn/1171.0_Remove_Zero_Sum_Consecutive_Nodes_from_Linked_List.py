'''
执行用时：32 ms, 在所有 Python3 提交中击败了99.19% 的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了33.33% 的用户
通过测试用例：105 / 105
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix = 0
        seen = {}
        seen[0] = dummy = ListNode(0)
        dummy.next = head 
        while head:
            prefix += head.val
            seen[prefix] = head 
            head = head.next 
        head = dummy 
        prefix = 0
        while head:
            prefix += head.val 
            head.next = seen[prefix].next 
            head = head.next 
        return dummy.next 
        