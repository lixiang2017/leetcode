'''
approach: Bidirectional BFS, Bidirectional Breadth-First Search
question: why can be bidirectional?
answer: It can be reversed/reversible no matter jumping from left node, right node or node with equal value. 
From the rear end, it will still be the same path.

data structure:
1. a graph, a precomputer dictionary
2. a visited-nodes set
3. curs, a list nodes for current processing; [other, the list of nodes from tail]
4. nex, a list nodes for next processing, to keep next layer nodes
5. step, the minimum number of steps to reach the last index of the array

Time: O(N) since we will visit every node at most once.
Space: O(N) since it needs graph/set/curs/nex to store nodes.

ref:
https://leetcode.com/problems/jump-game-iv/solution/
'''

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) <= 1:
            return 0
        
        size = len(arr)
        graph = {}
        visited = set([0, size - 1])
        curs = [0]  # store current layer
        other = [size - 1]  # store current layer from tail side
        nex = []
        step = 0
        
        # precompute
        for i in range(size):
            if arr[i] not in graph:
                graph[arr[i]] = [i]
            else:
                graph[arr[i]].append(i)
        
        # while current layer exists
        while curs:
            nex = []
            # search from the side with fewer nodes
            if len(curs) > len(other):
                curs, other = other, curs
            
            # iterate the layer
            for node in curs:
                # check if reached end
                # if node == len(arr) - 1:
                #     return step
                
                # children, the next layer   # check if child reach other
                for child in graph[arr[node]]:
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)
                
                # clear the list to avoid/prevent reduntant search
                graph[arr[node]] = []
                
                # check neighbors, left and right node
                for child in [node - 1, node + 1]:
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)
            
            curs = nex
            step += 1
        
        return -1
        