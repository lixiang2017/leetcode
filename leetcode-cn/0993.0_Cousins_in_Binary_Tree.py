'''
approach: DFS + DFS
Time: O(N + N) = O(N)
Space: O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了93.44% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了32.41% 的用户
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def getDepth(node, depth, num):
            if not node:
                return None
            if node.val == num:
                return depth
            return getDepth(node.left, depth + 1, num) or getDepth(node.right, depth + 1, num)
        
        def getParent(node, num):
            if not node:
                return None
            if (node.left and node.left.val == num) or (node.right and node.right.val == num):
                return node.val
            return getParent(node.left, num) or getParent(node.right, num)

        depthx, parentx = getDepth(root, 0, x), getParent(root, x)
        depthy, parenty = getDepth(root, 0, y), getParent(root, y)
        return (depthx == depthy) and (parentx != parenty)
