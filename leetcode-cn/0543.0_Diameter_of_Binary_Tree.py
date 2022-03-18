'''
DFS

执行用时：584 ms, 在所有 Python3 提交中击败了5.13% 的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了5.15% 的用户
通过测试用例：104 / 104
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0

        def get_depth(node: TreeNode):
            if not node:
                return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1

        def dfs(node: TreeNode, depth: int):
            if not node:
                return 0
            
            left_max = dfs(node.left, depth + 1)
            right_max = dfs(node.right, depth + 1)
            # through center
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            center = left_depth + right_depth
            return max(left_max, right_max, center)

        ans = dfs(root, 0)
        return ans 

