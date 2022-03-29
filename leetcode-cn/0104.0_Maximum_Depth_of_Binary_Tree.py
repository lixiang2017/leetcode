'''
DFS

执行用时：48 ms, 在所有 Python3 提交中击败了45.03% 的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了31.22% 的用户
通过测试用例：39 / 39
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
BFS

执行用时：48 ms, 在所有 Python3 提交中击败了45.03% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了85.35% 的用户
通过测试用例：39 / 39
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
        q, d = [root], 0
        while q:
            q = [child for node in q for child in (node.left, node.right) if child]
            d += 1
        return d 

