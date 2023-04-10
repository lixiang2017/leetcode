'''
monotonic stack

执行用时：244 ms, 在所有 Python3 提交中击败了15.54% 的用户
内存消耗：20.6 MB, 在所有 Python3 提交中击败了5.40% 的用户
通过测试用例：76 / 76
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        node = head
        n = 0
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
            n += 1
        ans = [0] * n
        stack = []  # (node, idx)
        i = 0
        node = head
        while node:
            while stack and stack[-1][0].val < node.val:
                ans[stack[-1][1]] = arr[i]
                stack.pop()
            stack.append((node, i))
            i += 1
            node = node.next
        return ans 
