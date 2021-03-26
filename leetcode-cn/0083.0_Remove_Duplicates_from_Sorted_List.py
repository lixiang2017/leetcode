'''
Time: O(N)
Space: O(1)


执行用时：36 ms, 在所有 Python 提交中击败了20.28%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了44.88%的用户
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            while cur and cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next

        return head
