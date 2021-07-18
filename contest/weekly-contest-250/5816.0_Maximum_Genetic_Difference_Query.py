'''
Time Limit Exceeded
'''
class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        for node, val in queries:
            xor = val ^ node
            while parents[node] != -1:
                xor = max(xor, val ^ parents[node])
                node = parents[node]            
            ans.append(xor)
        return ans
        