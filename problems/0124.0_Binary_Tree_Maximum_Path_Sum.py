'''
DFS

Runtime: 90 ms, faster than 93.09% of Python3 online submissions for Binary Tree Maximum Path Sum.
Memory Usage: 21.5 MB, less than 20.23% of Python3 online submissions for Binary Tree Maximum Path Sum.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        
        def subMaxSum(node):
            # max sum of one branch 
            if not node:
                return 0
            lsum = subMaxSum(node.left)
            rsum = subMaxSum(node.right)
            
            branch = node.val + max(lsum, rsum)
            max_branch = max(node.val, branch)
            nonlocal ans
            ans = max(ans, max_branch, lsum + node.val + rsum)
            return max_branch
    
        subMaxSum(root)
        return ans
    
'''

Input: [2,-1,-2]
Output: 1
Expected: 2


Input
[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]
Output
15
Expected
16
'''
    
