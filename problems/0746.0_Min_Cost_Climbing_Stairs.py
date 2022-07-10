'''
Success
Details 
Runtime: 36 ms, faster than 93.08% of Python online submissions for Min Cost Climbing Stairs.
Memory Usage: 13.5 MB, less than 33.98% of Python online submissions for Min Cost Climbing Stairs.
'''



class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) < 2:
            return 0
        
        cost += [0]  # must have
        size = len(cost)
        dp = [cost[0], cost[1]]
        for i in range(2, size):
            dp.append(min(dp[i - 1], dp[i -2]) + cost[i])
        
        return dp[-1]


'''
DP, in place
T: O(N)
S: O(1)

Runtime: 81 ms, faster than 63.67% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage: 14.1 MB, less than 44.40% of Python3 online submissions for Min Cost Climbing Stairs.
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 2], cost[i - 1])
        return min(cost[-1], cost[-2])
