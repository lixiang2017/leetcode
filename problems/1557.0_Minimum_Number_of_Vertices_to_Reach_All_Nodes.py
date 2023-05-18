'''
Runtime: 1209 ms, faster than 35.14% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
Memory Usage: 54.9 MB, less than 23.10% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
'''
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        for _from, _to in edges:
            in_degree[_to] += 1
        return [i for i in range(n) if in_degree[i] == 0]
        