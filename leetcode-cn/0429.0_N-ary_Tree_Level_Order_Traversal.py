'''
approach: BFS
Time: O(N)
Space: O(N)

执行用时：44 ms, 在所有 Python 提交中击败了48.84%的用户
内存消耗：15.9 MB, 在所有 Python 提交中击败了64.53%的用户
'''


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        q = [root]
        level = []
        while q:
            current_level_values = []
            next_level = []
            for node in q:
                for child in node.children:
                    next_level.append(child)
                current_level_values.append(node.val)
            level.append(current_level_values)
            q = next_level

        return level


'''
approach: BFS
T: O(N)
S: O(N)

执行用时：52 ms, 在所有 Python3 提交中击败了82.93% 的用户
内存消耗：16.8 MB, 在所有 Python3 提交中击败了76.37% 的用户
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = [root]
        while q:
            level = []
            next_q = []
            for node in q:
                level.append(node.val)
                next_q.extend(node.children)
            ans.append(level)
            q = next_q
            
        return ans 


'''
DFS

执行用时：56 ms, 在所有 Python3 提交中击败了65.17% 的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了29.48% 的用户
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []

        def dfs(node: Node, depth: int) -> None:
            if not node:
                return 
            if len(ans) <= depth:
                ans.append([])
            ans[depth].append(node.val)
            for ch in node.children:
                dfs(ch, depth + 1)
            
        dfs(root, 0)
        return ans 



