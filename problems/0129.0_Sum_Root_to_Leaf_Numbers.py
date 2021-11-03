'''
DFS

Runtime: 32 ms, faster than 72.26% of Python3 online submissions for Sum Root to Leaf Numbers.
Memory Usage: 14.4 MB, less than 18.39% of Python3 online submissions for Sum Root to Leaf Numbers.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node, x):
            nonlocal ans
            if not node:
                return
            for child in [node.left, node.right]:
                if child:
                    dfs(child, x * 10 + node.val)
            if not node.left and not node.right:
                ans += x * 10 + node.val
                
        dfs(root, 0)
        return ans


'''
BFS

Runtime: 28 ms, faster than 89.40% of Python3 online submissions for Sum Root to Leaf Numbers.
Memory Usage: 14 MB, less than 93.44% of Python3 online submissions for Sum Root to Leaf Numbers.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque()
        if root:
            q.append((root, 0))
        while q:
            node, x = q.popleft()
            for child in [node.left, node.right]:
                if child:
                    q.append((child, x * 10 + node.val))
            if not node.left and not node.right:
                ans += x * 10 + node.val

        return ans


