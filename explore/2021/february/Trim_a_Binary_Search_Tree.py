'''
approach: DFS / Recursion

Time: O(N), where N is the total number of nodes in the given tree. We visit each node at most once.
Space: O(N). Even though we don't explicityly use any additional memory. the call stack of our recursion
could be as large as the number of nodes in the worst case.

You are here!
Your runtime beats 92.43 % of python submissions.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if not root: return root
        
        if low <= root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            return self.trimBST(root.right, low, high)
        