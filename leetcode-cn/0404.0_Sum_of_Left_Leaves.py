'''
BFS
执行用时：52 ms, 在所有 Python3 提交中击败了7.19% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了93.71% 的用户
通过测试用例：100 / 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0
        q = deque([root]) if root else []
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                if not node.left.left and not node.left.right:
                    ans += node.left.val
            if node.right:
                q.append(node.right)
                
        return ans 

'''
DFS

执行用时：40 ms, 在所有 Python3 提交中击败了42.22% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了39.83% 的用户
通过测试用例：100 / 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0 

        def dfs(node: TreeNode):
            if not node:
                return 
            if node.left:
                if not node.left.left and not node.left.right:
                    nonlocal ans 
                    ans += node.left.val 
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans 

