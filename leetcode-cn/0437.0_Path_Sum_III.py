'''
DFS

执行用时：304 ms, 在所有 Python3 提交中击败了39.56% 的用户
内存消耗：35.4 MB, 在所有 Python3 提交中击败了15.52% 的用户
通过测试用例：126 / 126
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        ans = 0

        def dfs(node: TreeNode, paths):
            nonlocal ans
            if not node:
                return 
            next_path = []
            for p in paths:
                if p + node.val == targetSum:
                    ans += 1
                next_path.append(p + node.val)
            # just node.val
            if node.val == targetSum:
                ans += 1
            next_path.append(node.val)

            dfs(node.left, next_path)
            dfs(node.right, next_path)

        dfs(root, [])
        return ans
