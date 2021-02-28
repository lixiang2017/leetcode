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
