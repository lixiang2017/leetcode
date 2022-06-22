'''
BFS

执行用时：52 ms, 在所有 Python3 提交中击败了52.25% 的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了47.67% 的用户
通过测试用例：76 / 76
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans, q = root.val, [root]
        while q:
            ans = q[0].val 
            q = [child for node in q for child in [node.left, node.right] if child]
        return ans 

'''
BFS2

执行用时：52 ms, 在所有 Python3 提交中击败了52.25% 的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了53.70% 的用户
通过测试用例：76 / 76
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans, q = -1, deque([root]) if root else deque()
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            ans = node.val 
        return ans 




'''
DFS

执行用时：36 ms, 在所有 Python3 提交中击败了99.21% 的用户
内存消耗：18.1 MB, 在所有 Python3 提交中击败了15.83% 的用户
通过测试用例：76 / 76
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = cur_depth = 0

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return 
            nonlocal ans, cur_depth
            if depth > cur_depth:
                cur_depth = depth 
                ans = node.val 
            depth += 1
            dfs(node.left, depth)
            dfs(node.right, depth)
        
        dfs(root, 1)
        return ans 

'''
DFS2

执行用时：52 ms, 在所有 Python3 提交中击败了52.25% 的用户
内存消耗：18 MB, 在所有 Python3 提交中击败了24.31% 的用户
通过测试用例：76 / 76
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = cur_depth = 0

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return 
            depth += 1
            dfs(node.left, depth)
            dfs(node.right, depth)
            nonlocal ans, cur_depth
            if depth > cur_depth:
                cur_depth = depth 
                ans = node.val 
                        
        dfs(root, 1)
        return ans 

