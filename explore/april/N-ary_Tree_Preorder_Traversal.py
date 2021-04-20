'''
approach: DFS / Recursion
Time: O(N), where N is the number of nodes in the given tree.
Space: O(N)

You are here!
Your runtime beats 7.38 % of python3 submissions.
You are here!
Your memory usage beats 63.08 % of python3 submissions.
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]: 
        def pre(node: 'Node') :
            if not node:
                return
            yield node.val
            for child in node.children:
                yield from pre(child)
        
        return list(pre(root))
        