'''
DFS

执行用时：44 ms, 在所有 Python3 提交中击败了63.46% 的用户
内存消耗：21.1 MB, 在所有 Python3 提交中击败了63.46% 的用户
通过测试用例：28 / 28
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: TreeNode, _max: int, _min: int) -> None:
            if not node:
                return 
            nonlocal ans
            _max = max(_max, node.val)
            _min = min(_min, node.val)
            ans = max(ans, _max - _min)
            dfs(node.left, _max, _min)
            dfs(node.right, _max, _min)

        dfs(root, root.val, root.val)
        return ans 
