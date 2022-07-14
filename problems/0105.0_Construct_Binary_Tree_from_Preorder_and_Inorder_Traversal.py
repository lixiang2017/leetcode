'''
Runtime: 193 ms, faster than 63.17% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 18.9 MB, less than 76.63% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        def construct(prel, prer, inl, inr):
            if prel > prer:
                return None 
            if prel == prer:
                return TreeNode(preorder[prel])
            root = TreeNode(preorder[prel])
            idx = inorder.index(preorder[prel], inl, inr + 1)
            # left_part in inorder   inl...idx-1
            left_len = idx - inl 
            # right_part in inorder  idx+1...inr 
            # right_len = inr - idx 
            root.left = construct(prel + 1, prel + left_len, inl, idx - 1)
            root.right = construct(prel + left_len + 1, prer, idx + 1, inr)
            return root
        
        return construct(0, n - 1, 0, n - 1)
