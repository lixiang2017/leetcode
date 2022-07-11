'''
BFS

Runtime: 62 ms, faster than 22.04% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 13.9 MB, less than 69.82% of Python3 online submissions for Binary Tree Right Side View.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        row = [root] if root else []
        while row:
            right_view.append(row[-1].val)
            row = [child for node in row for child in [node.left, node.right] if child]    
        return right_view
    
'''
DFS

Runtime: 52 ms, faster than 46.10% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 13.9 MB, less than 22.93% of Python3 online submissions for Binary Tree Right Side View.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
    
        def dfs(node, depth):
            if not node:
                return 
            if len(right_view) < depth:
                right_view.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 1)
        return right_view

'''
DFS

Runtime: 53 ms, faster than 43.71% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 13.9 MB, less than 22.93% of Python3 online submissions for Binary Tree Right Side View.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
    
        def dfs(node, depth):
            if not node:
                return 
            if len(right_view) < depth:
                right_view.append(node.val)
            elif len(right_view) >= depth:
                right_view[depth - 1] = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root, 1)
        return right_view
    
