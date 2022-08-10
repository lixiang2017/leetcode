'''
DFS
T: O(N)
S: O(logN)

Runtime: 121 ms, faster than 62.24% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.6 MB, less than 32.22% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left, right):
            if left > right:
                return None 
            if left == right:
                return TreeNode(nums[left])
            mid = (left + right) // 2
            return TreeNode(nums[mid], dfs(left, mid - 1), dfs(mid + 1, right))
        
        return dfs(0, len(nums) - 1)
