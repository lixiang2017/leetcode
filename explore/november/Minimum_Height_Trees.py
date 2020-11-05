'''
You are here!
Your runtime beats 87.77 % of python submissions.
'''


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # base cases
        if n <= 2:
            return [i for i in range(n)]
        
        # build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        
        # init 
        leaves = []
        for i in range(n):
            if 1 == len(neighbors[i]):
                leaves.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                for neighbor in neighbors[leaf]:
                    neighbors[neighbor].remove(leaf)
                    if 1 == len(neighbors[neighbor]):
                        new_leaves.append(neighbor)
            
            leaves = new_leaves
            
        return leaves
    