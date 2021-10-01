'''
DFS

You are here!
Your runtime beats 88.65 % of python3 submissions.
You are here!
Your memory usage beats 86.91 % of python3 submissions.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        i = len(nums) // 2
        root = TreeNode(nums[i])
        root.left = self.sortedArrayToBST(nums[: i])
        root.right = self.sortedArrayToBST(nums[i + 1:])
        return root
        
