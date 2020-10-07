'''
BFS

You are here!
Your runtime beats 34.88 % of python submissions.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        q = deque()
        q.append(root)
        q.append(root)
        while q:
            node1 = q.popleft()
            node2 = q.popleft()
            
            if node1 == None and node2 == None:
                continue
            
            if node1 == None or node2 == None:
                return False
            
            if node1.val != node2.val:
                return False
            
            q.append(node1.left)
            q.append(node2.right)
            q.append(node1.right)
            q.append(node2.left)
        
        return True
