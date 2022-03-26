'''
sort

Runtime: 47 ms, faster than 75.12% of Python3 online submissions for Two City Scheduling.
Memory Usage: 13.9 MB, less than 45.30% of Python3 online submissions for Two City Scheduling.
'''
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # (ai - bi, i)
        n2 = len(costs)
        n = n2 // 2
        diff = [(a - b, i) for i, (a, b) in enumerate(costs)]
        diff.sort()
        sum_a = sum([costs[diff[idx][1]][0] for idx in range(n)])
        sum_b = sum([costs[diff[idx][1]][1] for idx in range(n, n2)])
        return sum_a + sum_b
        
