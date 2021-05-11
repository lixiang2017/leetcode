'''
approach: BFS

You are here!
Your runtime beats 98.73 % of python submissions.
You are here!
Your memory usage beats 96.34 % of python submissions.
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
        if root is None:
            return []
        
        rightView = []
        q = deque([root])
        while q:
            
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    rightView.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return rightView
        