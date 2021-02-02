'''
no need to know the number of nodes in every level

You are here!
Your runtime beats 60.58 % of python submissions.
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
        
        q = [root]
        tail = root
        while q:
            node = q.pop(0)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            
            if node == tail:
                node.next = None
                tail = q[-1] if q else None
            else:
                node.next = q[0]
        
        return root
    