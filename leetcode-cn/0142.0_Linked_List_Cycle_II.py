'''
two pointers

执行用时：48 ms, 在所有 Python3 提交中击败了90.74% 的用户
内存消耗：18.5 MB, 在所有 Python3 提交中击败了83.29% 的用户
通过测试用例：17 / 17
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head 
        while True:
            if not (fast and fast.next):
                return None 
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                break
        fast = head 
        while slow != fast:
            slow = slow.next 
            fast = fast.next
        return slow
        
