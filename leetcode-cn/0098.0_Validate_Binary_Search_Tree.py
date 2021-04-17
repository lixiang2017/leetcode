'''
approach: DFS + In Order Traverse
Time: O(N + N) = O(N), where N is the number of nodes in the given tree.
Space: O(N)

执行用时：144 ms, 在所有 Python3 提交中击败了7.71%的用户
内存消耗：17.5 MB, 在所有 Python3 提交中击败了35.58%的用户
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inOrder(node):
            if not node:
                return None
            yield from inOrder(node.left)
            yield node.val
            yield from inOrder(node.right)
        
        in_order = list(inOrder(root))
        N = len(in_order)
        for i in range(N - 1):
            if in_order[i] >= in_order[i + 1]:
                return False

        return True
