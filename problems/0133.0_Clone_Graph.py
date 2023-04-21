'''
Runtime: 50 ms, faster than 56.86% of Python3 online submissions for Clone Graph.
Memory Usage: 14.7 MB, less than 34.46% of Python3 online submissions for Clone Graph.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return deepcopy(node)
        


'''
DFS

Runtime: 40 ms, faster than 83.75% of Python3 online submissions for Clone Graph.
Memory Usage: 14.4 MB, less than 66.44% of Python3 online submissions for Clone Graph.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        # val -> cloned_node
        self.seen = dict()
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if node.val in self.seen:  
            return self.seen[node.val]
        
        cnode = Node(node.val)
        self.seen[node.val] = cnode
        # a connected undirected graph, all neighbors not None. No!!!
        if node.neighbors:
            cnode.neighbors = []
            for neigh in node.neighbors:
                cneigh = self.cloneGraph(neigh)
                cnode.neighbors.append(cneigh)
        
        return cnode
    

'''
Runtime: 46 ms, faster than 63.44% of Python3 online submissions for Clone Graph.
Memory Usage: 14.4 MB, less than 91.72% of Python3 online submissions for Clone Graph.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        # val -> cloned_node
        self.seen = dict()
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if node.val in self.seen:  
            return self.seen[node.val]
        
        cnode = Node(node.val, [])
        self.seen[node.val] = cnode
        # a connected undirected graph, all neighbors not None. No!!!
        for neigh in node.neighbors:
            cneigh = self.cloneGraph(neigh)
            cnode.neighbors.append(cneigh)
        
        return cnode
    
'''
Runtime: 41 ms, faster than 52.94% of Python3 online submissions for Clone Graph.
Memory Usage: 14.4 MB, less than 17.48% of Python3 online submissions for Clone Graph.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        seen = {}
        def dfs(node):
            if node.val in seen:
                return seen[node.val]
            cnode = Node(node.val, [])
            seen[node.val] = cnode
            for child in node.neighbors:
                cchild = dfs(child)
                cnode.neighbors.append(cchild)
            return cnode
                
        return dfs(node)


    
  
