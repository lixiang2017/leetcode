'''
approach: DFS
Time: O(V + E), where V is the number of vertexes and E is the number of edges.
Space: O(V)


You are here!
Your runtime beats 95.71 % of python submissions.
You are here!
Your memory usage beats 23.93 % of python submissions.
'''


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n
        global valid
        valid = True
        
        def dfs(node, nodeColor):
            global valid
            color[node] = nodeColor
            complement = (GREEN if nodeColor == RED else RED)
            for neighbor in graph[node]:
                if color[neighbor] == UNCOLORED:
                    dfs(neighbor, complement)
                    if not valid:
                        return
                elif color[neighbor] != complement:
                    valid = False
                    return
        
        for i in range(n):
            if color[i] == UNCOLORED:
                dfs(i, RED)
                if not valid:
                    break
                    
        return valid


'''
approach: BFS
Time: O(V + E)
Space: O(V)

You are here!
Your runtime beats 55.05 % of python submissions.
You are here!
Your memory usage beats 47.44 % of python submissions.
'''

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n
    
        for i in range(n):
            if color[i] == UNCOLORED:
                q = collections.deque([i])
                color[i] = RED
                while q:
                    node = q.popleft()
                    complement = (GREEN if color[node] == RED else RED)
                    for neighbor in graph[node]:
                        if color[neighbor] == UNCOLORED:
                            q.append(neighbor)
                            color[neighbor] = complement
                        elif color[neighbor] != complement:
                            return False
        return True
        


    