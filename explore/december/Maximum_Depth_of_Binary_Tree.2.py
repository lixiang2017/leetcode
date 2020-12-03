'''
BFS 
# no need to know the length of deque

You are here!
Your runtime beats 56.72 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        depth = 0
        while queue:
            # qlength = len(queue)
            # for i in range(qlength):
            node, depth = queue.popleft()
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return depth
        