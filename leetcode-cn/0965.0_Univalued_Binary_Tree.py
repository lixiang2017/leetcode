'''
iterative inorder

执行用时：32 ms, 在所有 Python3 提交中击败了93.20% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了97.06% 的用户
通过测试用例：72 / 72
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True 
        v = root.val 

        def inorder(node):
            stack = []
            while node or stack:
                if node:
                    stack.append(node)
                    node = node.left 
                else:
                    node = stack.pop()
                    yield node.val 
                    node = node.right 

        for val in inorder(root):
            if val != v:
                return False 
        return True 
