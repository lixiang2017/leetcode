'''
Success
Details
Runtime: 20 ms, faster than 88.94% of Python online submissions for Symmetric Tree.
Memory Usage: 13.1 MB, less than 21.09% of Python online submissions for Symmetric Tree.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(tree1, tree2):
            if not tree1 or not tree2:
                return tree1 == tree2

            if tree1.val != tree2.val:
                return False

            return isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)   

        if not root:
            return True
        return isMirror(root.left, root.right)


if __name__ == '__main__':
    t = TreeNode(val=1, 
        left=TreeNode(val=2, 
            left=TreeNode(val=3), right=TreeNode(val=4)), 
        right=TreeNode(val=2, 
            left=TreeNode(val=3), right=TreeNode(val=4)))
    assert not Solution().isSymmetric(t)

    t = TreeNode(val=1, 
        left=TreeNode(val=2, 
            left=TreeNode(val=3), right=TreeNode(val=4)), 
        right=TreeNode(val=2, 
            left=TreeNode(val=4), right=TreeNode(val=3)))
    assert Solution().isSymmetric(t)

    t = TreeNode(val=1, 
        left=TreeNode(val=2, 
            right=TreeNode(val=3)), 
        right=TreeNode(val=2, 
            right=TreeNode(val=3)))
    assert not Solution().isSymmetric(t)

