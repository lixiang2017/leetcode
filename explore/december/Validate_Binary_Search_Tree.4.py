'''
approach 2: iterative traversal with valid range
time: O(N) since we visit each node exactly once.
space: O(N) since we keep up to entire tree.

Success
Details
Runtime: 52 ms, faster than 5.24% of Python online submissions for Validate Binary Search Tree.
Memory Usage: 18 MB, less than 64.69% of Python online submissions for Validate Binary Search Tree.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        stack = [(root, -sys.maxint, sys.maxint)]
        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue
            val = node.val
            if val <= lower or val >= upper:
                return False
            
            stack.append((node.left, lower, val))
            stack.append((node.right, val, upper))
            
        return True
    