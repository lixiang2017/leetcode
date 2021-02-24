'''
approach: DFS(post order traversal)
Time: O(N), where N is the number of nodes.
Space: O(height)

执行结果：
通过
显示详情
执行用时：36 ms, 在所有 Python 提交中击败了82.44%的用户
内存消耗：17.7 MB, 在所有 Python 提交中击败了58.78%的用户
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """        
        return self.isBalancedWithDepth(root, 1)[0]

    def isBalancedWithDepth(self, node, depth):
        if not node:
            return True, depth

        lefted, leftDepth = self.isBalancedWithDepth(node.left, depth + 1)
        righted, rightDepth = self.isBalancedWithDepth(node.right, depth + 1)
        if lefted and righted:
            diff = abs(leftDepth - rightDepth)
            if diff <= 1:
                return True, max(leftDepth, rightDepth)

        return False, max(leftDepth, rightDepth)
