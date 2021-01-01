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
        # DFS recursively
        if not node:
            return node
        
        memo = {node: Node(node.val)}
        self.dfs(node, memo)
        return memo[node]
    
    def dfs(self, node, memo):
        for neighbor in node.neighbors:
            if neighbor not in memo:
                memo[neighbor] = Node(neighbor.val)
                self.dfs(neighbor, memo)
            memo[node].neighbors.append(memo[neighbor])
        