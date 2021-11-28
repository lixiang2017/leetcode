'''
86 mstime cost
8.74 MBmemory cost
Your submission beats78.80 %Submissions
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import heapq

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        nums = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)

        dfs(root)
        return heapq.nsmallest(k, nums, lambda x: abs(x - target))

