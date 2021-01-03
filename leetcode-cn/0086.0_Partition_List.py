'''
Time: O(N * 2) = O(N)
Space: O(N)

执行结果：
通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了81.79% 的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了11.33% 的用户
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
        lessThan = []
        greaterEqual = []

        while head:
            if head.val < x:
                lessThan.append(head.val)
            else:
                greaterEqual.append(head.val)
            head = head.next
        
        lessThan.extend(greaterEqual)
        lessThan = lessThan[:: -1]
        # print lessThan
        prev = None
        while lessThan:
            value = lessThan.pop(0)
            # print value
            prev = ListNode(val=value, next=prev)

        return prev
