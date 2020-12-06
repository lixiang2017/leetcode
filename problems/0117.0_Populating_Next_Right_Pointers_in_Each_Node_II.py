'''
Success
Details 
Runtime: 36 ms, faster than 81.43% of Python online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 16 MB, less than 37.29% of Python online submissions for Populating Next Right Pointers in Each Node II.
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
        