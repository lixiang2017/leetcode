'''
no need to handle the tail node of every level,
cause the default value of tail node's next pointer is None

You are here!
Your runtime beats 81.43 % of python submissions.
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if i < size - 1: curr.next = q[0]
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
        
        return root
        