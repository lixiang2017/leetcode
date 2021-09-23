'''
T:O(2N), S:O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了49.47% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了41.64% 的用户
通过测试用例：43 / 43
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        L = self.getLen(head)
        q, r = divmod(L, k)
        ans = []
        nth = 0
        node = head
        while node:
            ans.append(node)
            x = 0
            need = q - 1
            if nth < r:
                need += 1 
            while node and x < need:
                node = node.next
                x += 1
            # split
            next_node = node.next
            node.next = None
            node = next_node
            nth += 1

        ans += [None] * (k - nth)
        return ans

    def getLen(self, node):
        n = 0
        while node:
            n += 1
            node = node.next
        return n


'''
use pre ptr
T:O(2N), S:O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了70.74% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了64.89% 的用户
通过测试用例：43 / 43
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        L = self.getLen(head)
        q, r = divmod(L, k)
        ans = []
        nth = 0
        pre = node = head
        while node:
            ans.append(node)
            x = 0
            need = q
            if nth < r:
                need += 1 
            while node and x < need:
                pre = node
                node = node.next
                x += 1
            # split
            pre.next = None
            nth += 1

        ans += [None] * (k - nth)
        return ans

    def getLen(self, node):
        n = 0
        while node:
            n += 1
            node = node.next
        return n

