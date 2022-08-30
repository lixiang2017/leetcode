'''
DFS

Runtime: 200 ms, faster than 96.68% of Python3 online submissions for Maximum Binary Tree.
Memory Usage: 14.4 MB, less than 88.99% of Python3 online submissions for Maximum Binary Tree.
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
        return TreeNode(val = nums[idx], 
                        left = self.constructMaximumBinaryTree(nums[: idx]), 
                        right = self.constructMaximumBinaryTree(nums[idx + 1: ]))
