'''
Time: O(N)
Space: O(1)

执行用时：28 ms, 在所有 Python 提交中击败了61.22%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了11.13%的用户
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node and node.next and node.next.next:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None

'''
Time: O(1)
Space: O(1)

执行用时：24 ms, 在所有 Python 提交中击败了85.10%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了27.83%的用户
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
