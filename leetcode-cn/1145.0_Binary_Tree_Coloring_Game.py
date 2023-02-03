'''
greedy + DFS

执行用时：32 ms, 在所有 Python3 提交中击败了94.87% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了77.78% 的用户
通过测试用例：65 / 65
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        lsz = rsz = 0

        def dfs(node):
            if not node:
                return 0
            ls = dfs(node.left)
            rs = dfs(node.right)
            if node.val == x:
                nonlocal lsz, rsz 
                lsz, rsz = ls, rs 
            return ls + rs + 1
        
        dfs(root)
        return 2 * max(lsz, rsz, n - 1 - lsz - rsz) > n 
        
