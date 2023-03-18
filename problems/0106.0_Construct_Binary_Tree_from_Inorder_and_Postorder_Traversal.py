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


'''
DFS

Runtime: 99 ms, faster than 64.34% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 19 MB, less than 70.03% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        
        def construct(inleft: int, inright: int, postleft: int, postright: int) -> Optional[TreeNode]:
            if inleft > inright:
                return None
            val = postorder[postright]
            node = TreeNode(val)
            idx = inorder.index(val)
            left_len = idx - inleft
            # right_len = inright - idx
            node.left = construct(inleft, idx - 1, postleft, postleft + left_len - 1)
            node.right = construct(idx + 1, inright, postleft + left_len, postright - 1)
            return node
        
        return construct(0, n - 1, 0, n - 1)


'''
Runtime: 97 ms, faster than 64.55% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 19 MB, less than 70.03% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        
        def construct(inleft: int, inright: int, postleft: int, postright: int) -> Optional[TreeNode]:
            if inleft > inright:
                return None
            val = postorder[postright]
            node = TreeNode(val)
            idx = inorder.index(val, inleft, inright + 1)
            left_len = idx - inleft
            node.left = construct(inleft, idx - 1, postleft, postleft + left_len - 1)
            node.right = construct(idx + 1, inright, postleft + left_len, postright - 1)
            return node
        
        return construct(0, n - 1, 0, n - 1)


        