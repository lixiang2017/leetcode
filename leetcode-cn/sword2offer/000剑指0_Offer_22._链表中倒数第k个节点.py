'''
Two Pointers
其中一个指针先走k步
T: O(N)
S: O(1)

执行用时：28 ms, 在所有 Python3 提交中击败了93.01% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了77.33% 的用户
通过测试用例：208 / 208
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        a = b = head
        while k:
            a = a.next
            k -= 1
        while a:
            a = a.next
            b = b.next
        return b

'''
Two Pass

执行用时：32 ms, 在所有 Python3 提交中击败了79.59% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了45.49% 的用户
通过测试用例：208 / 208
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        node, n = head, 0
        while node:
            n += 1
            node = node.next
        node = head
        for _ in range(n - k):
            node = node.next
        return node
