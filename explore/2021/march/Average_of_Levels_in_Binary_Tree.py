'''
approach: BFS
Time: O(N), where N is the number of nodes in the given binary tree.
Space: O(N)

You are here!
Your runtime beats 50.25 % of python submissions.
You are here!
Your memory usage beats 51.97 % of python submissions
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        averages = []
        q = [root]
        while q:
            level_nodes = []
            current_sum = 0
            for node in q:
                current_sum += node.val
                if node.left:
                    level_nodes.append(node.left)
                if node.right:
                    level_nodes.append(node.right)
            averages.append(current_sum * 1.0 / len(q))
            # next level
            q = level_nodes
        
        return averages
    