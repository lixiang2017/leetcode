'''
DFS

Runtime: 36 ms, faster than 56.94% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.9 MB, less than 48.54% of Python3 online submissions for Sum of Left Leaves.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node: Optional[TreeNode], position: int):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right and position == -1:
                ans += node.val
            dfs(node.left, -1)
            dfs(node.right, 1)
            
        dfs(root, 0)        
        return ans


'''
BFS

Runtime: 32 ms, faster than 80.36% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.7 MB, less than 62.49% of Python3 online submissions for Sum of Left Leaves.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        # (node, position)  # -1: left, 0: root, 1: right
        q = deque([(root, 0)])
        while q:
            node, p = q.popleft()
            if not node.left and not node.right and p == -1:
                ans += node.val
            if node.left:
                q.append((node.left, -1))
            if node.right:
                q.append((node.right, 1))
                
        return ans


