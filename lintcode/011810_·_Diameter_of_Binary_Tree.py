'''
Accepted
100%
81 mstime cost
5.95 MBmemory cost
Your submission beats95.20 %Submissions
'''

from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        # write your code here
        ans = 0
        # for a certain node, dfs return its longest path from the_current_node to all of its leaves
        def dfs(node: TreeNode) -> int:
            nonlocal ans
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            ans = max(ans, l + r)
            return max(l, r) + 1

        dfs(root)
        return ans 
