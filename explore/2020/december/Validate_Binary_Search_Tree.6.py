'''
approach 4: iterative inorder traversal
time: O(N) in the worst case ehen the tree is BST or the "bad" element is a rightmost leaf.
space: O(N) to keep stack.

Success
Details
Runtime: 40 ms, faster than 32.01% of Python online submissions for Validate Binary Search Tree.
Memory Usage: 17.9 MB, less than 64.69% of Python online submissions for Validate Binary Search Tree.
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
        stack, prev = [], -sys.maxint
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True
    