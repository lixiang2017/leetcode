'''
T: O(2N), S:O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了76.20% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了14.76% 的用户
通过测试用例：26 / 26
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        q = deque()

        def dfs(node):
            if not node: return 
            q.append(node)
            dfs(node.child)
            dfs(node.next)
        
        dfs(head)
        for i in range(len(q) - 1):
            q[i].next = q[i + 1]
            q[i + 1].prev = q[i]
            q[i].child = None
        return head
