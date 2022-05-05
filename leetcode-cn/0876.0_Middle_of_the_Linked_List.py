'''
执行用时：40 ms, 在所有 Python3 提交中击败了40.67% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了89.81% 的用户
通过测试用例：36 / 36
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        return slow 
        
        