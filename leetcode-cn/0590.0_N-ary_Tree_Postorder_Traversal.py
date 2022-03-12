'''
approach: DFS
Time: O(N)
Space: O(N)

执行用时：52 ms, 在所有 Python 提交中击败了18.40%的用户
内存消耗：16 MB, 在所有 Python 提交中击败了34.43%的用户
'''


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        post = []
        for child in root.children:
            childPost = self.postorder(child)
            post += childPost
        post += [root.val]

        return post

'''
approach: DFS
Time: O(N)
Space: O(N)

执行用时：60 ms, 在所有 Python3 提交中击败了20.64% 的用户
内存消耗：17.2 MB, 在所有 Python3 提交中击败了5.46% 的用户
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
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        for child in root.children:
            ans.extend(self.postorder(child))
        ans.append(root.val)
        return ans 

'''
iteration, stack
Time: O(N)
Space: O(N)

执行用时：64 ms, 在所有 Python3 提交中击败了11.51% 的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了15.18% 的用户
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
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children)
        return ans[:: -1]


