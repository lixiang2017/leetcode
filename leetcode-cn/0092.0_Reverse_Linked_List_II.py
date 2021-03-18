'''
approach: reconstruct linked list 
Time: O(N + N) = O(N)
Space: O(N)

执行用时：16 ms, 在所有 Python 提交中击败了85.52%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了61.55%的用户
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        rearrange = values[: left - 1] + values[left - 1: right][:: -1] + values[right :]
        dummy = node = ListNode()
        for value in rearrange:
            node.next = ListNode(val=value)
            node = node.next

        return dummy.next
