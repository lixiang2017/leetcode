'''
DFS

Runtime: 35 ms, faster than 45.26% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.3 MB, less than 11.50% of Python3 online submissions for Invert Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
'''
BFS

Runtime: 36 ms, faster than 44.00% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.4 MB, less than 11.50% of Python3 online submissions for Invert Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = deque([root])
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root
        

'''
BFS

Runtime: 28 ms, faster than 91.21% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.3 MB, less than 11.50% of Python3 online submissions for Invert Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left
                q.append(node.left)
                q.append(node.right)
        return root
        
'''
DFS

Runtime: 38 ms, faster than 33.89% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.9 MB, less than 7.55% of Python3 online submissions for Invert Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

'''
one-liner

Runtime: 34 ms, faster than 59.87% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.8 MB, less than 94.98% of Python3 online submissions for Invert Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left)) if root else None
