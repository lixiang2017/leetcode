'''
BFS,T:O(N),S:O(N)

You are here!
Your runtime beats 68.27 % of python3 submissions.
You are here!
Your memory usage beats 86.48 % of python3 submissions.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        ans = [[root.val]]
        q = deque([(root)])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                for child in node.children:
                    level.append(child.val)
                    q.append(child)
            if level:
                ans.append(level)
        return ans

'''
BFS,T:O(N),S:O(N)

You are here!
Your runtime beats 38.92 % of python3 submissions.
You are here!
Your memory usage beats 61.08 % of python3 submissions.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans, q = [], [root]
        while any(q):
            ans.append([node.val for node in q])
            q = [child for node in q for child in node.children]
        return ans

'''
BFS,T:O(N),S:O(N)

You are here!
Your runtime beats 96.04 % of python3 submissions.
You are here!
Your memory usage beats 97.69 % of python3 submissions.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = [root]
        while q:
            next_q = [child for node in q for child in node.children]
            ans.append([node.val for node in q])
            q = next_q
        return ans





