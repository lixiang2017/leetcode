'''
You are here!
Your runtime beats 65.02 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        level_order = []
        q = deque()
        q.append(root)
        while q:
            one_level = []
            level_size = len(q)
            for i in xrange(level_size):
                one_node = q.popleft()
                one_level.append(one_node.val)

                if one_node.left:
                    q.append(one_node.left)

                if one_node.right:
                    q.append(one_node.right)
                    
            level_order.append(one_level)
        
        return level_order
        