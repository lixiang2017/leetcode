'''
DFS

执行用时：100 ms, 在所有 Python3 提交中击败了5.30% 的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了39.29% 的用户
通过测试用例：24 / 24
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:

        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node
                yield from inorder(node.right)
        
        prev = None 
        for node in inorder(root):
            if prev == p:
                return node 
            prev = node 
        return None
