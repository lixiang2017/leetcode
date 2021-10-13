'''
Runtime: 82 ms, faster than 5.14% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
Memory Usage: 14.4 MB, less than 12.48% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        
        def construct(prel: int, prer: int, inl: int, inr: int) -> Optional[TreeNode]:
            if prel > prer:
                return None
            idx = bisect_left(inorder, preorder[prel], inl, inr + 1)
            left_len, right_len = idx - inl + 1, inr - idx
            return TreeNode(val=preorder[prel], 
                            left=construct(prel + 1, prel + left_len - 1, inl, idx - 1),
                            right=construct(prel + left_len, prer, idx + 1, inr))
        
        return construct(0, len(preorder) - 1, 0, len(preorder) - 1)
