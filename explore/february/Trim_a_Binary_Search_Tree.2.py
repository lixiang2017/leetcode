'''
approach: Iteration / Iterative / BFS
Time: O(N), where N is the total number of nodes in the given tree. We visit each node at most once.
Space: O(len(q)), where q is the length for every level in the given tree, which is much less than N, the total number of nodes.

You are here!
Your runtime beats 78.33 % of python submissions.
You are here!
Your memory usage beats 75.46 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        # find the root
        while (root and (root.val < low or root.val > high)):
            if root.val < low:
                root = root.right
            if root.val > high:
                root = root.left
        
        if not root: return None
        
        q = [root]
        while q:
            node = q.pop(0)
            # find the left and right child of the current node
            left_node = node.left
            while left_node and left_node.val < low:
                left_node = left_node.right
            node.left = left_node
            
            right_node = node.right
            while right_node and right_node.val > high:
                right_node = right_node.left
            node.right = right_node
            
            if left_node: q.append(left_node)
            if right_node: q.append(right_node)
        
        return root
                