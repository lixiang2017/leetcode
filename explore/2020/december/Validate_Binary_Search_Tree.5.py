'''
approach 3: recursive inorder traversal

time: O(N) in the worst case when the tree is a BST or the "bad" element is a rightmost leaf
space: O(N) for the space on the run-time stack.

Success
Details
Runtime: 32 ms, faster than 83.77% of Python online submissions for Validate Binary Search Tree.
Memory Usage: 18.4 MB, less than 7.91% of Python online submissions for Validate Binary Search Tree.
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
        self.prev = -sys.maxint
        
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)
        
        return inorder(root)
