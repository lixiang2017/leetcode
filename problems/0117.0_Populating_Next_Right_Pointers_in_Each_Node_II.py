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



'''
BFS
T: O(N)
S: O(L), length of level

Runtime: 106 ms, faster than 6.48% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 15.4 MB, less than 48.93% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None 
        q = [root]
        while q:
            next_q = [child for node in q for child in [node.left, node.right] if child]
            if len(next_q) > 1:
                for i in range(len(next_q) - 1):
                    next_q[i].next = next_q[i + 1]
            q = next_q
        return root 


'''
recursion + hash table
T: O(N)
S: O(H), height of tree


Runtime: 88 ms, faster than 20.31% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 15.3 MB, less than 48.93% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
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
    def connect(self, root: 'Node') -> 'Node':
        # level -> node
        level2node = {}
        
        def dfs(node, level):
            if not node:
                return 
            if level not in level2node:
                level2node[level] = node
            else:
                level2node[level].next = node
                level2node[level] = node
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        dfs(root, 0)
        return root 





