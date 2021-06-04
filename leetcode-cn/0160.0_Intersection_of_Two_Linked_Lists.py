'''
Time: O(N)
Space: O(1)

执行用时：216 ms, 在所有 Python3 提交中击败了5.44% 的用户
内存消耗：29.5 MB, 在所有 Python3 提交中击败了79.57% 的用户
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A1, B1 = headA, headB
        while (A1 or B1) and (A1 != B1):
            if not A1:
                A1 = headB
            else:
                A1 = A1.next
            if not B1:
                B1 = headA
            else:
                B1 = B1.next
        
        return A1