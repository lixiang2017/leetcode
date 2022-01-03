'''

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
        root_bak = root
        while root and root.left:
            next_level = root.left
            while root:
                root.left.next = root.right 
                root.right.next = root.next and root.next.left
                root = root.next
        
            root = next_level
        
        return root_bak


'''
Runtime: 63 ms, faster than 59.16% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.8 MB, less than 31.97% of Python3 online submissions for Populating Next Right Pointers in Each Node.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque([root])
        while q:
            next_q = deque()
            node = q.popleft()
            for child in [node.left, node.right]:
                if child:
                    next_q.append(child)
            for _ in range(len(q)):
                right_node = q.popleft()
                for child in [right_node.left, right_node.right]:
                    if child:
                        next_q.append(child)
                node.next = right_node
                node = right_node
            q = next_q
            
        return root

