'''
DFS

执行用时：88 ms, 在所有 Python3 提交中击败了12.87% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了7.05% 的用户
通过测试用例：27 / 27
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root 

'''
iteration

执行用时：76 ms, 在所有 Python3 提交中击败了46.05% 的用户
内存消耗：18.9 MB, 在所有 Python3 提交中击败了22.25% 的用户
通过测试用例：27 / 27
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while True:
            if node.val < p.val and node.val < q.val:
                node = node.right 
            elif node.val > p.val and node.val > q.val:
                node = node.left 
            else:
                return node 
        return None 
        
