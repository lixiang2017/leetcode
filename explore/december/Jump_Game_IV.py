'''
approach: BFS, Breadth-First Search

data structure:
1. a graph, a precomputer dictionary
2. a visited-nodes set
3. curs, a list nodes for current processing
4. nex, a list nodes for next processing, to keep next layer nodes
5. step, the minimum number of steps to reach the last index of the array

Time: O(N) since we will visit every node at most once.
Space: O(N) since it needs graph/set/curs/nex to store nodes.

ref:
https://leetcode.com/problems/jump-game-iv/solution/

You are here!
Your runtime beats 61.11 % of python submissions.
You are here!
Your memory usage beats 62.50 % of python submissions.
'''

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) <= 1:
            return 0
        
        graph = {}
        visited = set([0])
        curs = [0]  # store current layer
        nex = []
        step = 0
        
        # precompute
        size = len(arr)
        for i in range(size):
            if arr[i] not in graph:
                graph[arr[i]] = [i]
            else:
                graph[arr[i]].append(i)
        
        # while current layer exists
        while curs:
            nex = []
            
            # iterate the layer
            for node in curs:
                # check if reached end
                if node == len(arr) - 1:
                    return step
                
                # children, the next layer
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)
                
                # clear the list to avoid/prevent reduntant search
                graph[arr[node]] = []
                
                # check neighbors, left and right node
                for child in [node - 1, node + 1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)
            
            curs = nex
            step += 1
        
        return -1
        