'''
DFS

执行用时：36 ms, 在所有 Python3 提交中击败了59.71% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了76.07% 的用户
通过测试用例：77 / 77
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

'''
BFS

执行用时：44 ms, 在所有 Python3 提交中击败了10.68% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了81.25% 的用户
通过测试用例：77 / 77
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = deque()
        if root:
            q.append(root)
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            for child in [node.left, node.right]:
                if child:
                    q.append(child)

        return root
