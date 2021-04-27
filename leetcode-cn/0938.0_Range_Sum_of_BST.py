'''
approach: DFS
Time: O(N)
Space: O(1)

执行用时：456 ms, 在所有 Python3 提交中击败了5.37% 的用户
内存消耗：23.1 MB, 在所有 Python3 提交中击败了11.28% 的用户
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 
            yield from dfs(node.left)
            yield node.val
            yield from dfs(node.right)
        
        return sum(value for value in dfs(root) if low <= value <= high)
        
