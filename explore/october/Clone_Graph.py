'''
You are here!
Your runtime beats 56.79 % of python submissions.
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # BFS
        if not node:
            return node
        
        memo = {node: Node(node.val)}
        deque = collections.deque([node])
        while deque:
            n = deque.popleft()
            for neighbor in n.neighbors:
                if neighbor not in memo:
                    deque.append(neighbor)  # to store the original link
                    memo[neighbor] = Node(neighbor.val)
                memo[n].neighbors.append(memo[neighbor])   # to recover the original link
        
        return memo[node]
        