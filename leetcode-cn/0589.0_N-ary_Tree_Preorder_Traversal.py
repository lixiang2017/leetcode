'''
approach: DFS
Time: O(N)
Space: O(N)

执行用时：48 ms, 在所有 Python 提交中击败了35.93%的用户
内存消耗：16.1 MB, 在所有 Python 提交中击败了11.98%的用户
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        pre = [root.val]
        for child in root.children:
            childPre = self.preorder(child)
            # pre.extend(childPre)  # also ok
            pre += childPre

        return pre


'''
DFS

执行用时：52 ms, 在所有 Python3 提交中击败了62.83% 的用户
内存消耗：16.9 MB, 在所有 Python3 提交中击败了52.01% 的用户
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
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        
        def dfs(node: 'Node'):
            if not node:
                return 
            ans.append(node.val)
            for child in node.children:
                dfs(child)

        dfs(root)
        return ans

'''
DFS

执行用时：44 ms, 在所有 Python3 提交中击败了97.13% 的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了46.53% 的用户
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
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        ans = [root.val]
        for child in root.children:
            ans.extend(self.preorder(child))
        return ans 


'''
iterative way

执行用时：52 ms, 在所有 Python3 提交中击败了75.34% 的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了45.06% 的用户
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
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(reversed(node.children))
        return ans 

'''
iterative way

执行用时：60 ms, 在所有 Python3 提交中击败了27.72% 的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了40.55% 的用户
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
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children[:: -1])
        return ans 

