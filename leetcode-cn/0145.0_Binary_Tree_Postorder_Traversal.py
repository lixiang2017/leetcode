'''
approach: DFS
Time: O(N)
Space: O(N)

执行用时：20 ms, 在所有 Python 提交中击败了54.47%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了61.29%的用户
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        post = []
        post += self.postorderTraversal(root.left)
        post += self.postorderTraversal(root.right)
        post += [root.val]
        return post


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        post = []
        if root:
            post += self.postorderTraversal(root.left)
            post += self.postorderTraversal(root.right)
            post += [root.val]
        return post            





'''
# Python3
执行用时：32 ms, 在所有 Python3 提交中击败了94.92%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了47.40%的用
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return list(self.post(root))

    def post(self, node):
        if node:
            yield from self.post(node.left)
            yield from self.post(node.right)
            yield node.val 