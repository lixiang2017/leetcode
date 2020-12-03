'''
python3   # yield from

Success
Details
Runtime: 28 ms, faster than 83.05% of Python3 online submissions for Increasing Order Search Tree.
Memory Usage: 14.1 MB, less than 61.02% of Python3 online submissions for Increasing Order Search Tree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        
        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        
        return ans.right        

