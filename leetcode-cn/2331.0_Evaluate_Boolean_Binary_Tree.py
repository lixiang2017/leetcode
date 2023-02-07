'''
执行用时：56 ms, 在所有 Python3 提交中击败了79.52% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了36.15% 的用户
通过测试用例：75 / 75
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left:
            return root.val == 1
        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)
        return l or r if root.val == 2 else l and r

