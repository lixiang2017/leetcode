'''
BFS
T: O(N)
S: O(N)

Runtime: 55 ms, faster than 91.41% of Python3 online submissions for N-ary Tree Level Order Traversal.
Memory Usage: 15.9 MB, less than 94.71% of Python3 online submissions for N-ary Tree Level Order Traversal.
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
        ans = []
        q = [root] if root else []
        while q:
            next_q = []
            level = []
            for node in q:
                level.append(node.val)
                next_q.extend(node.children)
            ans.append(level)
            q = next_q
        return ans 
        
