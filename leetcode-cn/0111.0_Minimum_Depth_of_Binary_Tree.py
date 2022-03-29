'''
DFS

执行用时：572 ms, 在所有 Python3 提交中击败了14.58% 的用户
内存消耗：57 MB, 在所有 Python3 提交中击败了22.12% 的用户
通过测试用例：52 / 52
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif root.left and not root.right:
            return 1 + self.minDepth(root.left)
        elif (not root.left) and root.right:
            return 1 + self.minDepth(root.right)
        elif root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


'''
BFS

执行用时：508 ms, 在所有 Python3 提交中击败了41.89% 的用户
内存消耗：51.7 MB, 在所有 Python3 提交中击败了79.68% 的用户
通过测试用例：52 / 52
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q, d = deque([root]), 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return d + 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            d += 1
        return d 
