'''
approach: Deque
Time: O(N), where N is the number of nodes in the given binary tree.
Space: O(2 * h + h) = O(h), where h is the height of binary tree.

You are here!
Your runtime beats 70.63 % of python submissions.
You are here!
Your memory usage beats 80.70 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        right = []
        if not root: return []
        # q = [(root, 1)] # (node, level)
        q = deque([(root, 1)])

        while q:
            # node, level = q.pop(0)
            node, level = q.popleft()
            if len(right) < level:
                right.append(node.val)
            else:
                right[level - 1] = node.val
                
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            
        return right
