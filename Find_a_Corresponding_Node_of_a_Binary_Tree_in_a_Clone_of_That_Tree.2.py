'''
BFS 2

You are here!
Your runtime beats 89.09 % of python submissions.
You are here!
Your memory usage beats 33.94 % of python submissions
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        target_value = target.val
        cloned_deque = deque([cloned])
        while cloned_deque:
            node = cloned_deque.popleft()
            if not node: # no need for  if node.left and if node.right
                continue
            if node.val == target_value:
                return node
            
            # if node.left:
            cloned_deque.append(node.left)
            # if node.right:
            cloned_deque.append(node.right)
