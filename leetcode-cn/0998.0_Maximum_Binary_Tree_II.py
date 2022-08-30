'''
simulation + DFS

执行用时：36 ms, 在所有 Python3 提交中击败了82.20% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了22.03% 的用户
通过测试用例：75 / 75
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val 
                yield from inorder(node.right)
        
        arr = list(inorder(root)) + [val]

        def construct(arr):
            if not arr:
                return None 
            idx = arr.index(max(arr))
            return TreeNode(val = arr[idx], left = construct(arr[: idx]), right = construct(arr[idx + 1: ]))

        return construct(arr)
