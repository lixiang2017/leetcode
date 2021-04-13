'''
approach: Traverse In Order

执行用时：36 ms, 在所有 Python3 提交中击败了88.12%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了66.36%的用户
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        values = []
        def inorder(node):
            if not node:
                return
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)
        
        for val in inorder(root):
            values.append(val)

        N = len(values)
        minDiff = sys.maxsize
        for i in range(N - 1):
            diff = abs(values[i + 1] - values[i])
            minDiff = min(minDiff, diff)
            if minDiff == 0:
                return 0
        return minDiff
