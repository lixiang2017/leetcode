'''
DFS

执行用时：56 ms, 在所有 Python3 提交中击败了35.04% 的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了50.43% 的用户
通过测试用例：160 / 160
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        # only root
        if not root.left and not root.right:
            return str(root.val)
        # only root and right 
        if not root.left:
            return str(root.val) + '()' + '(' + self.tree2str(root.right) + ')'
        # only root and left
        if not root.right:
            return str(root.val) + '(' + self.tree2str(root.left) + ')'
        return str(root.val) + '(' + self.tree2str(root.left) + ')' + '(' + self.tree2str(root.right) + ')' 


'''
DFS

执行用时：56 ms, 在所有 Python3 提交中击败了34.56% 的用户
内存消耗：17.4 MB, 在所有 Python3 提交中击败了23.51% 的用户
通过测试用例：160 / 160
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node):
            if not node:
                return ''
            ans = str(node.val)
            if node.left or node.right:
                ans += '(' + dfs(node.left) + ')'
            if node.right:
                ans += '(' + dfs(node.right) + ')'
            return ans 

        return dfs(root)

