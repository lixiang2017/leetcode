'''
approach: DFS
Time: O(N + N) = O(N)
Space: O(N)

执行用时：44 ms, 在所有 Python3 提交中击败了41.27%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了75.54%的用户
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode):
            if not node:
                return
            yield from dfs(node.left)
            yield node.val
            yield from dfs(node.right)
        
        dummy = head = TreeNode()
        for value in dfs(root):
            head.right = TreeNode(val=value)
            head = head.right

        return dummy.right
