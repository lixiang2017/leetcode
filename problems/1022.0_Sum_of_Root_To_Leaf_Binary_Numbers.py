'''
DFS

Runtime: 58 ms, faster than 17.55% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
Memory Usage: 14.7 MB, less than 39.83% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode], x: int):
            nonlocal ans
            if not node:
                return
            if node.left:
                dfs(node.left, 2 * x + node.val)
            if node.right:
                dfs(node.right, 2 * x + node.val)
            if not node.left and not node.right:
                ans += 2 * x + node.val
                
        dfs(root, 0)
        return ans

'''
BFS

Runtime: 61 ms, faster than 14.85% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
Memory Usage: 14.6 MB, less than 68.44% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque()
        if root:
            q.append((root, root.val))
        while q:
            node, x = q.popleft()
            if node.left:
                q.append((node.left, 2 * x + node.left.val))
            if node.right:
                q.append((node.right, 2 * x + node.right.val))
            if not node.left and not node.right:
                ans += x
            
        return ans
