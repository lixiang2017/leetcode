'''
DFS

执行用时：292 ms, 在所有 Python3 提交中击败了94.69% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了76.37% 的用户
通过测试用例：71 / 71
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans 
            if not node:
                return 0
            p_len = 0
            max_branch = 0
            L = dfs(node.left)
            if node.left and node.left.val == node.val:
                p_len += 1 + L
                max_branch = 1 + L 
            R = dfs(node.right)
            if node.right and node.right.val == node.val:
                p_len += 1 + R
                max_branch = max(max_branch, 1 + R)
            ans = max(ans, p_len)
            return max_branch

        dfs(root)
        return ans 

'''
通过测试用例：43 / 71
输入：
[1,null,1,1,1,1,1,1]
输出：
6
预期结果：
4
'''



