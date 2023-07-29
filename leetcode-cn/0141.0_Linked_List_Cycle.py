'''
执行用时：60 ms, 在所有 Python3 提交中击败了74.63% 的用户
内存消耗：20.2 MB, 在所有 Python3 提交中击败了22.60% 的用户
通过测试用例：23 / 23
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while slow and fast:
            slow = slow.next 
            if fast.next:
                fast = fast.next.next
            else:
                break
            if slow == fast:
                return True
        return False 

'''
执行用时：64 ms, 在所有 Python3 提交中击败了58.51% 的用户
内存消耗：20.2 MB, 在所有 Python3 提交中击败了24.49% 的用户
通过测试用例：23 / 23
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True
        return False
