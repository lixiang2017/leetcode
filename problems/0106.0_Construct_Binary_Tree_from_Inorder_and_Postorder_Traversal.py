'''
DFS

Runtime: 203 ms, faster than 23.04% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 88.5 MB, less than 22.93% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        
        root = TreeNode(val=postorder[-1])
        idx = inorder.index(postorder[-1])

        # left subtree
        root.left = self.buildTree(inorder[: idx], postorder[: idx])
        
        # right subtree
        root.right = self.buildTree(inorder[idx + 1: ], postorder[idx: -1])
        
        return root
