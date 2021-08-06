'''
BFS
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 90.88 % of python3 submissions.
You are here!
Your memory usage beats 88.82 % of python3 submissions.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([(root, root.val, [root.val])])  # (node, curr_sum, [path_to_curr])
        while q:
            node, curr_sum, path_to_curr = q.popleft()
            if not node.left and not node.right and curr_sum == targetSum:
                ans.append(path_to_curr)
                
            for child in [node.left, node.right]:
                if child:
                    q.append((child, curr_sum + child.val, path_to_curr + [child.val]))
        
        return ans

'''
DFS
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 30.01 % of python3 submissions.
You are here!
Your memory usage beats 14.63 % of python3 submissions.
'''
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def dfs(node: TreeNode, curr_sum: int, path_to_curr: List[int]):
            if not node:
                return
            if not node.left and not node.right and curr_sum == targetSum:
                ans.append(path_to_curr)
            for child in [node.left, node.right]:
                if child:
                    dfs(child, curr_sum + child.val, path_to_curr + [child.val])
                    
        dfs(root, root.val, [root.val])
        return ans
    
