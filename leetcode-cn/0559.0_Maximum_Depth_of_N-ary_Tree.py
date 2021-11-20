'''
DFS

执行用时：52 ms, 在所有 Python3 提交中击败了28.79% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了83.43% 的用户
通过测试用例：38 / 38
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ans = 0

        def dfs(node: 'Node', depth):
            nonlocal ans
            if not node:
                return
            ans = max(ans, depth + 1)
            for child in node.children:
                dfs(child, depth + 1)

        dfs(root, 0)
        return ans

'''
BFS

执行用时：40 ms, 在所有 Python3 提交中击败了89.50% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了83.43% 的用户
通过测试用例：38 / 38
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        step = 0
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
            step += 1
        return step 

