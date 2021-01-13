'''
Follow up: Solve the problem if repeated values on the tree are allowed.
target.val is useless, and we should compare target node (the pointer) with one node in original.

BFS
You are here!
Your runtime beats 46.06 % of python submissions.
You are here!
Your memory usage beats 20.00 % of python submissions.
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
        # target_value = target.val
        two_deque = deque()
        two_deque.append((original, cloned))
        while two_deque:
            two_nodes = two_deque.popleft()
            if not two_nodes[0]: # no need for  if node.left and if node.right
                continue
            if two_nodes[0] == target:
                return two_nodes[1]
            
            # if node.left:
            two_deque.append((two_nodes[0].left, two_nodes[1].left))
            # if node.right:
            two_deque.append((two_nodes[0].right, two_nodes[1].right))
                              