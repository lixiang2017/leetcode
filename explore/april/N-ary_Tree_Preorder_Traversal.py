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


'''
approach: One Line / DFS

You are here!
Your runtime beats 5.51 % of python3 submissions.
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
        return list(chain([root.val], *[self.preorder(child) for child in root.children])) if root else []



'''
approach: DFS / Recursion

You are here!
Your runtime beats 22.72 % of python3 submissions.
You are here!
Your memory usage beats 63.59 % of python3 submissions.
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
        if not root:
            return []
        
        ans = [root.val]
        for child in root.children:
            ans += self.preorder(child)
        return ans


'''
approach: BFS
Time: O(N), where N is the number of nodes in the given tree.
Space: O(N)

You are here!
Your runtime beats 98.51 % of python3 submissions.
You are here!
Your memory usage beats 88.44 % of python3 submissions.
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
        if not root:
            return []
        
        stack, output = [root, ], []
        while stack:
            node = stack.pop(-1)
            output.append(node.val)
            stack.extend(node.children[:: -1])
        
        return output
