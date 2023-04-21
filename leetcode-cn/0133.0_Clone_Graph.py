'''
BFS

执行用时：40 ms, 在所有 Python3 提交中击败了82.23% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了16.38% 的用户
通过测试用例：22 / 22
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None 
        seen = {node.val: Node(node.val, [])}
        q = deque([node])
        while q:
            x = q.popleft()
            for y in x.neighbors:
                if y.val not in seen:
                    q.append(y)
                    seen[y.val] = Node(y.val, [])
                seen[x.val].neighbors.append(seen[y.val])

        return seen[node.val]

