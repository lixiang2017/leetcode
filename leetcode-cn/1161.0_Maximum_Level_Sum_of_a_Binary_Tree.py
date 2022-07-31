'''
BFS

执行用时：252 ms, 在所有 Python3 提交中击败了89.03% 的用户
内存消耗：19.4 MB, 在所有 Python3 提交中击败了98.06% 的用户
通过测试用例：40 / 40
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        nodes = [root]
        s = root.val 
        ans = 1 
        level = 1
        while nodes:
            nxt_nodes = []
            cur_s = 0
            for node in nodes:
                if node.left:
                    nxt_nodes.append(node.left)
                if node.right:
                    nxt_nodes.append(node.right)
                cur_s += node.val 
            if cur_s > s:
                s = cur_s 
                ans = level 
            level += 1
            nodes = nxt_nodes
            
        return ans


'''
DFS

执行用时：316 ms, 在所有 Python3 提交中击败了27.74% 的用户
内存消耗：19.4 MB, 在所有 Python3 提交中击败了98.06% 的用户
通过测试用例：40 / 40
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = defaultdict(int)
        def dfs(node, level):
            if not node:
                return 
            level_sum[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)
        return max(level_sum.keys(), key=level_sum.__getitem__)


'''
执行用时：276 ms, 在所有 Python3 提交中击败了50.97% 的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了52.90% 的用户
通过测试用例：40 / 40
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        s = []
        def dfs(node, level):
            if not node:
                return 
            if level == len(s):
                s.append(node.val)
            else:
                s[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return s.index(max(s)) + 1
