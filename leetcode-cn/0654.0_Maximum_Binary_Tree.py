'''
DFS

执行用时：140 ms, 在所有 Python3 提交中击败了18.40% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了58.47% 的用户
通过测试用例：107 / 107
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None 
        idx = nums.index(max(nums))
        t = TreeNode(val=nums[idx])
        t.left = self.constructMaximumBinaryTree(nums[: idx])
        t.right = self.constructMaximumBinaryTree(nums[idx + 1: ])
        return t 
