'''
DFS

执行用时：40 ms, 在所有 Python3 提交中击败了42.11% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了42.11% 的用户
通过测试用例：225 / 225
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = []

        def preorder(node: TreeNode):
            if node:
                pre.append(node)
                preorder(node.left)
                preorder(node.right)
        
        preorder(root)
        for i in range(1, len(pre)):
            prev, curr = pre[i - 1], pre[i]
            prev.right = curr
            prev.left = None


'''
Iteration for preorder

执行用时：24 ms, 在所有 Python3 提交中击败了99.41% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了73.93% 的用户
通过测试用例：225 / 225
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = []
        stack = []
        node = root

        while node or stack:
            while node:
                pre.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

        for i in range(1, len(pre)):
            prev, curr = pre[i-1], pre[i]
            prev.left = None
            prev.right = curr


'''
Iteration, for preorder

执行用时：24 ms, 在所有 Python3 提交中击败了99.41% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了73.93% 的用户
通过测试用例：225 / 225
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = []
        stack = []
        node = root

        while node or stack:
            while node:
                pre.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

        for i in range(1, len(pre)):
            prev, curr = pre[i-1], pre[i]
            prev.left = None
            prev.right = curr


'''
like Morris, T:O(N) S:O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了42.11% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了94.28% 的用户
通过测试用例：225 / 225
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.right = nxt
                curr.left = None

            curr = curr.right
