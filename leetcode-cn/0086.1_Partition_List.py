'''
approach: two pointers

Time: O(N)
Space: O(1)

执行结果：通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了60.93%的用户
内存消耗：
13.1 MB, 在所有 Python 提交中击败了25.00%的用户
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lessDummy = less = ListNode(0)
        greaterDummy = greater = ListNode(0)

        while head:
            next_node = head.next
            head.next = None
            if head.val < x:
                less.next = head
                less = less.next
                # less.next = None
            else:
                greater.next = head
                greater = greater.next
                # greater.next = None

            # head = head.next
            head = next_node

        less.next = greaterDummy.next
        
        return lessDummy.next
