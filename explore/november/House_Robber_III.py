'''
You are here!
Your runtime beats 79.68 % of python submissions.
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.dp(root)
        return max(res[0], res[1])
    
    def dp(self, Node):
        if not Node:
            return [0, 0]
        
        left = self.dp(Node.left)
        right = self.dp(Node.right)
        
        rob = Node.val + left[0] + right[0]
        not_rob = max(left[0], left[1]) + max(right[0], right[1])
        return [not_rob, rob]
    