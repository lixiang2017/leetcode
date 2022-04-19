'''
iteration for post order

执行用时：68 ms, 在所有 Python3 提交中击败了48.45% 的用户
内存消耗：17.4 MB, 在所有 Python3 提交中击败了76.35% 的用户
通过测试用例：215 / 215
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        postsum, node, stack = 0, root, []
        while node or stack:
            if node:
                stack.append(node)
                node = node.right 
            else:
                node = stack.pop()
                postsum += node.val 
                node.val = postsum 
                node = node.left 
        
        return root 
