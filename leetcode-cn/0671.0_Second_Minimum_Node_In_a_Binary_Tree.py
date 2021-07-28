'''
Hash Set + DFS + Sort

执行用时：32 ms, 在所有 Python3 提交中击败了87.88% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了7.57% 的用户
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        seen = set()
        def dfs(node: TreeNode):
            if not node:
                return 
            seen.add(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        if len(seen) == 1:
            return -1
        else:
            return sorted(list(seen))[1]
