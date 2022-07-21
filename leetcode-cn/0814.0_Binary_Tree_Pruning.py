'''
DFS

执行用时：36 ms, 在所有 Python3 提交中击败了79.14% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了14.71% 的用户
通过测试用例：30 / 30
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            if 0 == l:
                node.left = None 
            r = dfs(node.right)
            if 0 == r:
                node.right = None 
            return l or r or node.val 

        v = dfs(root)
        if 0 == v:
            return None 
        else:
            return root 


'''
DFS

执行用时：52 ms, 在所有 Python3 提交中击败了8.02% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了33.42% 的用户
通过测试用例：30 / 30
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None 
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left is None and root.right is None and root.val == 0:
            return None 
        return root 


