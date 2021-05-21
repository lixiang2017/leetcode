'''
approach: BFS / deque
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 98.64 % of python3 submissions.
You are here!
Your memory usage beats 96.56 % of python3 submissions.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return []
        
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            levels.append(level)    
        
        return levels
        