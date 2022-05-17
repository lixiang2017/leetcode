'''
DFS

Runtime: 906 ms, faster than 29.29% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
Memory Usage: 24 MB, less than 40.41% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or not target:
            return None 
        if original == target:
            return cloned 
        return self.getTargetCopy(original.left, cloned.left, target) or \
                self.getTargetCopy(original.right, cloned.right, target)
        
