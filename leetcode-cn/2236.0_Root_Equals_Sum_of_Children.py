'''
执行用时：32 ms, 在所有 Python3 提交中击败了91.65% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.54% 的用户
通过测试用例：309 / 309
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val 
        