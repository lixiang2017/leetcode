'''
BFS

执行用时：168 ms, 在所有 Python3 提交中击败了95.37% 的用户
内存消耗：19.4 MB, 在所有 Python3 提交中击败了21.61% 的用户
通过测试用例：39 / 39
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = [root] if root else []
        while q:
            ans = sum(node.val for node in q)
            q = [child for node in q for child in [node.left, node.right] if child]
        return ans 


'''
DFS

执行用时：180 ms, 在所有 Python3 提交中击败了74.38% 的用户
内存消耗：19.3 MB, 在所有 Python3 提交中击败了41.05% 的用户
通过测试用例：39 / 39
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans, max_d = 0, -1
        def walk(node, d):
            nonlocal ans, max_d
            if not node:
                return 
            if max_d < d:
                max_d = d 
                ans = node.val 
            elif max_d == d:
                ans += node.val 
            walk(node.left, d + 1)
            walk(node.right, d + 1)

        walk(root, 0)
        return ans 


'''
DFS2

执行用时：264 ms, 在所有 Python3 提交中击败了23.15% 的用户
内存消耗：19.2 MB, 在所有 Python3 提交中击败了63.58% 的用户
通过测试用例：39 / 39
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def walk(node, d):
            _sum, depth = 0, d - 1
            if not node:
                return _sum, depth 
            _sum1, depth1 = walk(node.left, d + 1)
            _sum2, depth2 = walk(node.right, d + 1)
            depth = max(depth, depth1, depth2)
            if depth == depth1:
                _sum += _sum1 
            if depth == depth2:
                _sum += _sum2
            if depth == d:
                _sum += node.val
            return _sum, depth 

        return walk(root, 0)[0]



