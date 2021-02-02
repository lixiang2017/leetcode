'''
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
        
        root_bak = root
        q = deque([root])
        while q:
            level_size = len(q)
            for i in range(level_size - 1):
                q[i].next = q[i + 1]
                if q[i].left: q.append(q[i].left)
                if q[i].right: q.append(q[i].right)
                # q.popleft()
                
            q[level_size - 1].next = None
            if q[level_size - 1].left: q.append(q[level_size - 1].left)
            if q[level_size - 1].right: q.append(q[level_size - 1].right) 
            for i in range(level_size):
                q.popleft()
        
        return root_bak
