'''
DFS, inorder
T: O(k), S: O(H)

执行用时：48 ms, 在所有 Python3 提交中击败了71.71% 的用户
内存消耗：18.7 MB, 在所有 Python3 提交中击败了61.62% 的用户
通过测试用例：93 / 93
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        ans = -1
        def inorder(node: Optional[TreeNode]) -> int:
            nonlocal i, ans
            if not node:
                return None
            inorder(node.left)
            i += 1
            if i == k:
                ans = node.val
                return 
            inorder(node.right)

        inorder(root)
        return ans



'''
执行用时：44 ms, 在所有 Python3 提交中击败了87.05% 的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了27.38% 的用户
通过测试用例：93 / 93
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node):
            if not node:
                return
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)
        
        it = inorder(root)
        for _ in range(k):
            ans = next(it)
        return ans

