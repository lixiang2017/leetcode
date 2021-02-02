'''
approach 1: recursive traversal with valid range
time: O(N) since we visit each node exactly once.
space: O(N) since we keep up to the entire tree.

Success
Details
Runtime: 40 ms, faster than 32.01% of Python online submissions for Validate Binary Search Tree.
Memory Usage: 18.2 MB, less than 17.21% of Python online submissions for Validate Binary Search Tree.
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
        def validate(node, low = -sys.maxint, high = sys.maxint):
            # Empty trees ares valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False
            
            # The left and right substree must also be valid.
            return validate(node.right, node.val, high) and \
                validate(node.left, low, node.val)
        
        return validate(root)