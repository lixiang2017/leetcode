'''
BFS
T: O(N)
S: O(N)

Runtime: 73 ms, faster than 20.09% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.2 MB, less than 94.47% of Python3 online submissions for Maximum Depth of Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        step = 0
        q = [root] if root else None
        while q: 
            q = [child for node in q for child in [node.left, node.right] if child]
            step += 1
        return step

'''
DFS

Runtime: 40 ms, faster than 89.54% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.3 MB, less than 31.05% of Python3 online submissions for Maximum Depth of Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


'''
DFS

Runtime: 90 ms, faster than 5.41% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.2 MB, less than 51.13% of Python3 online submissions for Maximum Depth of Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))
        
        return depth(root)


'''
DFS

Runtime: 62 ms, faster than 39.01% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.3 MB, less than 18.15% of Python3 online submissions for Maximum Depth of Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0


