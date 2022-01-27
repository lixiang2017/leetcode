'''
DFS

Runtime: 478 ms, faster than 42.55% of Python3 online submissions for All Elements in Two Binary Search Trees.
Memory Usage: 23.1 MB, less than 5.70% of Python3 online submissions for All Elements in Two Binary Search Trees.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def dfs(node: TreeNode):
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        
        nums1, nums2 = dfs(root1), dfs(root2)
        ans = []
        m, n = len(nums1), len(nums2)
        i = j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
                
        ans += nums1[i: ] + nums2[j: ]   
        return ans
