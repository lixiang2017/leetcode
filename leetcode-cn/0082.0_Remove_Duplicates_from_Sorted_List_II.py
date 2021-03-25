'''
approach: One Pass
Time: O(N)
Space: O(1)

执行用时：24 ms, 在所有 Python 提交中击败了88.94%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了46.14%的用户
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
        if not head:
            return head
        dummy = cur = ListNode(val=105, next=head)
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                # use x 
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next
