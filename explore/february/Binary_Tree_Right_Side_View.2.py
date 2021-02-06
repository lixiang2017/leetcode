'''
approach: DFS
Time: O(N), where N is the number of nodes in the given binary tree.
Space: O(N), where N is the number of nodes in the given binary tree.

You are here!
Your runtime beats 92.54 % of python submissions.
You are here!
Your memory usage beats 80.70 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        right = []
        
        def dfs(node, level):
            if not node:
                return 
            if len(right) < level:
                right.append(node.val)
            
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 1)
        
        return right
