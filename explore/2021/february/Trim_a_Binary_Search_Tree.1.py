'''
approach: Recursion / DFS
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 13.58 % of python submissions.
You are here!
Your memory usage beats 48.83 % of python submissions.
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
        def trim(node, low, high):
            if not node: return node

            if low <= node.val <= high:
                node.left = trim(node.left, low, high)
                node.right = trim(node.right, low, high)
                return node
            elif node.val > high:
                return trim(node.left, low, high)
            else:
                return trim(node.right, low, high)

        return trim(root, low, high)
