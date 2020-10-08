'''
You are here!
Your runtime beats 84.30 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        size = len(nums)
        def dfs(array, low, high):
            if low > high:
                return None
            
            mid = (low + high) / 2
            node = TreeNode(val = array[mid])
            node.left = dfs(array, low, mid - 1)
            node.right = dfs(array, mid + 1, high)
            
            return node
        
        return dfs(nums, 0 , size - 1)