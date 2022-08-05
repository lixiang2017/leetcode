'''
BFS

执行用时：56 ms, 在所有 Python3 提交中击败了31.71% 的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了88.78% 的用户
通过测试用例：109 / 109
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if 1 == depth:
            return TreeNode(val, root)
        nodes = [root]
        for _ in range(depth - 2):
            nodes = [child for node in nodes for child in [node.left, node.right] if child]

        for node in nodes:
            l = node.left 
            node.left = TreeNode(val, l)
            r = node.right 
            node.right = TreeNode(val, right=r)
        return root 
