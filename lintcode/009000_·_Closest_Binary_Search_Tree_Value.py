'''
102 mstime cost
8.75 MBmemory cost
Your submission beats31.20 %Submissions
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if not root:
            return -1
        ans = root.val
        def dfs(node: TreeNode):
            nonlocal ans
            if not node:
                return 
            if abs(node.val - target) <= abs(ans - target):
                ans = node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ans
