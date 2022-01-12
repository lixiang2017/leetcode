'''
DFS

Runtime: 208 ms, faster than 15.57% of Python3 online submissions for Insert into a Binary Search Tree.
Memory Usage: 16.8 MB, less than 59.81% of Python3 online submissions for Insert into a Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        def dfs(node, val):
            if not node:
                return 

            if node.val < val:
                if node.right:
                    dfs(node.right, val)
                else:
                    node.right = TreeNode(val)
                    return
            else:
                if node.left:
                    dfs(node.left, val)
                else:
                    node.left = TreeNode(val)
                    return 
                
        dfs(root, val)
        return root

'''
DFS
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        
        return root
        


'''
Iterative

Runtime: 181 ms, faster than 23.34% of Python3 online submissions for Insert into a Binary Search Tree.
Memory Usage: 16.9 MB, less than 26.36% of Python3 online submissions for Insert into a Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        p = root
        while p:
            if p.val < val:
                if not p.right:
                    p.right = TreeNode(val)
                    break
                else:
                    p = p.right
            else:
                if not p.left:
                    p.left = TreeNode(val)
                    break
                else:
                    p = p.left
        
        return root
        
