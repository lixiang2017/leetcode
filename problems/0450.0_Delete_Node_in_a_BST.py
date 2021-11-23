'''
Runtime: 115 ms, faster than 11.70% of Python3 online submissions for Delete Node in a BST.
Memory Usage: 18.5 MB, less than 62.37% of Python3 online submissions for Delete Node in a BST.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # to find target node and parent of target
        parent = None
        target = None
        # direction from parent to target
        direction = 0
        def find(_parent: Optional[TreeNode], node: Optional[TreeNode], direct: int):
            nonlocal target, parent, direction
            if (not node) or (target is not None):
                return 
            if node.val == key:
                parent = _parent
                target = node
                direction = direct
                return 
            find(node, node.left, -1)
            find(node, node.right, 1)
        
        find(None, root, direction)
        if not target:
            return root
        
        if target.right:
            r = target.right
            if r.left:
                prev = r
                while r.left:
                    prev = r
                    r = r.left
                target.val = r.val
                # to link with right subtree
                prev.left = r.right
            else:
                target.val = target.right.val
                target.right = target.right.right
        elif target.left:
            l = target.left
            if l.right:
                prev = l
                while l.right:
                    prev = l
                    l = l.right
                target.val = l.val
                # to link with left subtree
                prev.right = l.left
            else:
                target.val = target.left.val
                target.left = target.left.left      
        else:
            if 0 == direction:
                root = None
            elif 1 == direction:
                parent.right = None
            else: # -1 == direction
                parent.left = None
        return root 
         
